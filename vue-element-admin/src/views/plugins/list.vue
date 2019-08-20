<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.name" placeholder="name" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
        查找
      </el-button>
    </div>

    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%;"
      @sort-change="sortChange"
    >
      <el-table-column label="ID" prop="id" sortable="custom" align="center" width="80" :class-name="getSortClass('id')">
        <template slot-scope="scope">
          <span>{{ scope.row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="name" prop="name" sortable="custom" :class-name="getSortClass('name')" min-width="150px">
        <template slot-scope="{row}">
          <span class="link-type" @click="handleUpdate(row)">{{ row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="version" width="110px" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.version }}</span>
        </template>
      </el-table-column>
      <el-table-column label="config" width="150px" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.config }}</span>
        </template>
      </el-table-column>
      <el-table-column label="状态" width="150px" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.container | statusTagFilter">
            {{ scope.row.container | statusFilter }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="Actions" align="center" min-width="150px" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-button v-if="statusTagFilter(row.container)!='success'" type="primary" size="mini" @click="handleCreate(row)">
            安装
          </el-button>
          <el-button v-if="statusTagFilter(row.container)!='info'" type="warning" size="mini" @click="handleUpdate(row)">
            重装
          </el-button>
          <el-button v-if="statusTagFilter(row.container)!='info'" type="success" size="mini" @click="handleRestart(row)">
            重启
          </el-button>
          <el-button v-if="statusTagFilter(row.container)!='info'" size="mini" type="danger" @click="handleDelete(row)">
            卸载
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="70px" style="width: 400px; margin-left:50px;">
        <el-form-item label="自定义配置">
          <el-input v-model="temp.config" :autosize="{ minRows: 2, maxRows: 4}" type="textarea" placeholder="Please input" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          取消
        </el-button>
        <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">
          提交
        </el-button>
      </div>
    </el-dialog>

    <el-dialog :visible.sync="dialogPvVisible" title="Reading statistics">
      <el-table :data="pvData" border fit highlight-current-row style="width: 100%">
        <el-table-column prop="key" label="Channel" />
        <el-table-column prop="pv" label="Pv" />
      </el-table>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogPvVisible = false">Confirm</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { fetchList, setup, remove, restart } from '@/api/plugins'
import waves from '@/directive/waves' // waves directive
import Pagination from '@/components/Pagination' // secondary package based on el-pagination

const addInfo = {
  id: undefined,
  config: '{}'
}
export default {
  name: 'Plugins',
  components: { Pagination },
  directives: { waves },
  filters: {
    statusFilter(status) {
      if (status) {
        return '已安装'
      }
      return '未安装'
    },
    statusTagFilter(status) {
      if (status) {
        return 'success'
      }
      return 'info'
    }
  },
  data() {
    return {
      tableKey: 0,
      list: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        name: undefined,
        ordering: ''
      },
      showReviewer: false,
      temp: addInfo,
      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        update: 'Edit',
        create: 'Create'
      },
      dialogPvVisible: false,
      pvData: [],
      rules: {
        config: [{ required: true, message: 'config is required', trigger: 'blur' }]
      },
      downloadLoading: false
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      fetchList(this.listQuery).then(response => {
        // console.log(response)
        this.list = response.data.results
        this.total = response.data.count
        // Just to simulate the time of the request
        setTimeout(() => {
          this.listLoading = false
        }, 1.5 * 1000)
      }).catch(error => console.log(error))
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    sortChange(data) {
      const { prop, order } = data
      if (order === 'ascending') {
        this.listQuery.ordering = `${prop}`
      } else {
        this.listQuery.ordering = `-${prop}`
      }
      if (prop == null) {
        this.listQuery.ordering = ''
      }
      // console.log(prop)
      this.handleFilter()
    },
    resetTemp() {
      this.temp = addInfo
    },
    handleCreate(row) {
      this.temp = Object.assign({}, row) // copy obj
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp)
          setup(tempData).then(response => {
            this.dialogFormVisible = false
            if (response.status === 200) {
              this.$notify({
                title: 'Success',
                message: '安装成功',
                type: 'success',
                duration: 2000
              })
            } else {
              this.$notify({
                title: 'Error',
                message: response.data.detail[0] || 'Error',
                type: 'error',
                duration: 5000
              })
            }
            this.getList()
          })
        }
      })
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row) // copy obj
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp)
          tempData.re = 1
          this.listLoading = true
          setup(tempData).then(() => {
            for (const v of this.list) {
              if (v.id === this.temp.id) {
                const index = this.list.indexOf(v)
                this.list.splice(index, 1, this.temp)
                break
              }
            }
            this.dialogFormVisible = false
            this.$notify({
              title: 'Success',
              message: '重装成功',
              type: 'success',
              duration: 2000
            })
            this.listLoading = false
            this.getList()
          })
        }
      })
    },
    handleDelete(row) {
      // console.log(row.id)
      remove(row.id).then(response => {
        if (response.status === 200) {
          this.$notify({
            title: 'Success',
            message: '卸载成功',
            type: 'success',
            duration: 2000
          })
        } else {
          this.$notify({
            title: 'Error',
            message: response.data.detail[0] || 'Error',
            type: 'error',
            duration: 5000
          })
        }
        this.getList()
      })
    },
    handleRestart(row) {
      // console.log(row.id)
      restart(row.id).then(response => {
        if (response.status === 200) {
          this.$notify({
            title: 'Success',
            message: '重启成功',
            type: 'success',
            duration: 2000
          })
        } else {
          this.$notify({
            title: 'Error',
            message: response.data.detail[0] || 'Error',
            type: 'error',
            duration: 5000
          })
        }
        this.getList()
      })
    },
    getSortClass: function(key) {
      const sort = this.listQuery.ordering
      return sort === `${key}`
        ? 'ascending'
        : sort === `-${key}`
          ? 'descending'
          : ''
    },
    statusTagFilter(status) {
      if (status) {
        return 'success'
      }
      return 'info'
    }
  }
}
</script>
