(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-17e82a3c"],{"333d":function(e,t,a){"use strict";var n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"pagination-container",class:{hidden:e.hidden}},[a("el-pagination",e._b({attrs:{background:e.background,"current-page":e.currentPage,"page-size":e.pageSize,layout:e.layout,"page-sizes":e.pageSizes,total:e.total},on:{"update:currentPage":function(t){e.currentPage=t},"update:current-page":function(t){e.currentPage=t},"update:pageSize":function(t){e.pageSize=t},"update:page-size":function(t){e.pageSize=t},"size-change":e.handleSizeChange,"current-change":e.handleCurrentChange}},"el-pagination",e.$attrs,!1))],1)},i=[];a("c5f6");Math.easeInOutQuad=function(e,t,a,n){return e/=n/2,e<1?a/2*e*e+t:(e--,-a/2*(e*(e-2)-1)+t)};var o=function(){return window.requestAnimationFrame||window.webkitRequestAnimationFrame||window.mozRequestAnimationFrame||function(e){window.setTimeout(e,1e3/60)}}();function s(e){document.documentElement.scrollTop=e,document.body.parentNode.scrollTop=e,document.body.scrollTop=e}function l(){return document.documentElement.scrollTop||document.body.parentNode.scrollTop||document.body.scrollTop}function r(e,t,a){var n=l(),i=e-n,r=20,c=0;t="undefined"===typeof t?500:t;var u=function e(){c+=r;var l=Math.easeInOutQuad(c,n,i,t);s(l),c<t?o(e):a&&"function"===typeof a&&a()};u()}var c={name:"Pagination",props:{total:{required:!0,type:Number},page:{type:Number,default:1},limit:{type:Number,default:20},pageSizes:{type:Array,default:function(){return[10,20,30,50]}},layout:{type:String,default:"total, sizes, prev, pager, next, jumper"},background:{type:Boolean,default:!0},autoScroll:{type:Boolean,default:!0},hidden:{type:Boolean,default:!1}},computed:{currentPage:{get:function(){return this.page},set:function(e){this.$emit("update:page",e)}},pageSize:{get:function(){return this.limit},set:function(e){this.$emit("update:limit",e)}}},methods:{handleSizeChange:function(e){this.$emit("pagination",{page:this.currentPage,limit:e}),this.autoScroll&&r(0,800)},handleCurrentChange:function(e){this.$emit("pagination",{page:e,limit:this.pageSize}),this.autoScroll&&r(0,800)}}},u=c,p=(a("e498"),a("2877")),d=Object(p["a"])(u,n,i,!1,null,"6af373ef",null);t["a"]=d.exports},"43f2":function(e,t,a){"use strict";a.d(t,"g",function(){return i}),a.d(t,"c",function(){return o}),a.d(t,"l",function(){return s}),a.d(t,"f",function(){return l}),a.d(t,"h",function(){return r}),a.d(t,"a",function(){return c}),a.d(t,"j",function(){return u}),a.d(t,"d",function(){return p}),a.d(t,"i",function(){return d}),a.d(t,"b",function(){return m}),a.d(t,"k",function(){return f}),a.d(t,"e",function(){return h});var n=a("5a65");function i(e){return Object(n["a"])({url:"/vhosts/vhost/",method:"get",params:e,baseURL:"/v1"})}function o(e){return Object(n["a"])({url:"/vhosts/vhost/",method:"post",data:e,baseURL:"/v1"})}function s(e){return Object(n["a"])({url:"/vhosts/vhost/"+e.id+"/",method:"patch",data:e,baseURL:"/v1"})}function l(e){return Object(n["a"])({url:"/vhosts/vhost/"+e+"/",method:"delete",baseURL:"/v1"})}function r(e){return Object(n["a"])({url:"/vhosts/domain/",method:"get",params:e,baseURL:"/v1"})}function c(e){return Object(n["a"])({url:"/vhosts/domain/",method:"post",data:e,baseURL:"/v1"})}function u(e){return Object(n["a"])({url:"/vhosts/domain/"+e.id+"/",method:"patch",data:e,baseURL:"/v1"})}function p(e){return Object(n["a"])({url:"/vhosts/domain/"+e+"/",method:"delete",baseURL:"/v1"})}function d(e){return Object(n["a"])({url:"/vhosts/proxy/",method:"get",params:e,baseURL:"/v1"})}function m(e){return Object(n["a"])({url:"/vhosts/proxy/",method:"post",data:e,baseURL:"/v1"})}function f(e){return Object(n["a"])({url:"/vhosts/proxy/"+e.id+"/",method:"patch",data:e,baseURL:"/v1"})}function h(e){return Object(n["a"])({url:"/vhosts/proxy/"+e+"/",method:"delete",baseURL:"/v1"})}},"5a65":function(e,t,a){"use strict";a("6762");var n=a("bc3a"),i=a.n(n),o=a("5c96"),s=a("4360"),l=a("5f87");function r(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:void 0,a=[200,201,204,400,410,422];return a.includes(e.status)?e:401===e.status?(o["MessageBox"].confirm("You have been logged out, you can cancel to stay on this page, or log in again","Confirm logout",{confirmButtonText:"Re-Login",cancelButtonText:"Cancel",type:"warning"}).then(function(){s["a"].dispatch("user/resetToken").then(function(){location.reload()})}),Promise.reject(new Error(e.data||"Error"))):(404===e.status&&Object(o["Message"])({message:"资源不存在,或已删除",type:"error",duration:5e3}),t.request?console.log(t.request):console.log("Error",t.message),Object(o["Message"])({message:t.message||"Error",type:"error",duration:5e3}),console.log("err"+t),Promise.reject(t))}var c=i.a.create({baseURL:"/v1",timeout:5e3});c.interceptors.request.use(function(e){return s["a"].getters.token&&(e.headers["X-Token"]=Object(l["a"])()),e},function(e){return console.log(e),Promise.reject(e)}),c.interceptors.response.use(function(e){return r(e)},function(e){return r(e.response,e)}),t["a"]=c},6724:function(e,t,a){"use strict";a("8d41");var n="@@wavesContext";function i(e,t){function a(a){var n=Object.assign({},t.value),i=Object.assign({ele:e,type:"hit",color:"rgba(0, 0, 0, 0.15)"},n),o=i.ele;if(o){o.style.position="relative",o.style.overflow="hidden";var s=o.getBoundingClientRect(),l=o.querySelector(".waves-ripple");switch(l?l.className="waves-ripple":(l=document.createElement("span"),l.className="waves-ripple",l.style.height=l.style.width=Math.max(s.width,s.height)+"px",o.appendChild(l)),i.type){case"center":l.style.top=s.height/2-l.offsetHeight/2+"px",l.style.left=s.width/2-l.offsetWidth/2+"px";break;default:l.style.top=(a.pageY-s.top-l.offsetHeight/2-document.documentElement.scrollTop||document.body.scrollTop)+"px",l.style.left=(a.pageX-s.left-l.offsetWidth/2-document.documentElement.scrollLeft||document.body.scrollLeft)+"px"}return l.style.backgroundColor=i.color,l.className="waves-ripple z-active",!1}}return e[n]?e[n].removeHandle=a:e[n]={removeHandle:a},a}var o={bind:function(e,t){e.addEventListener("click",i(e,t),!1)},update:function(e,t){e.removeEventListener("click",e[n].removeHandle,!1),e.addEventListener("click",i(e,t),!1)},unbind:function(e){e.removeEventListener("click",e[n].removeHandle,!1),e[n]=null,delete e[n]}},s=function(e){e.directive("waves",o)};window.Vue&&(window.waves=o,Vue.use(s)),o.install=s;t["a"]=o},7456:function(e,t,a){},"8d41":function(e,t,a){},a7db:function(e,t,a){"use strict";a.r(t);var n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"app-container"},[a("div",{staticClass:"filter-container"},[a("el-input",{staticClass:"filter-item",staticStyle:{width:"200px"},attrs:{placeholder:"Domain"},nativeOn:{keyup:function(t){return!t.type.indexOf("key")&&e._k(t.keyCode,"enter",13,t.key,"Enter")?null:e.handleFilter(t)}},model:{value:e.listQuery.domain,callback:function(t){e.$set(e.listQuery,"domain",t)},expression:"listQuery.domain"}}),e._v(" "),a("el-select",{staticClass:"filter-item",staticStyle:{width:"90px"},attrs:{placeholder:"autossl",clearable:""},model:{value:e.listQuery.autossl,callback:function(t){e.$set(e.listQuery,"autossl",t)},expression:"listQuery.autossl"}},e._l(e.statusOptions,function(e){return a("el-option",{key:e.key,attrs:{label:e.display_name,value:e.key}})}),1),e._v(" "),a("el-select",{staticClass:"filter-item",staticStyle:{width:"130px"},attrs:{placeholder:"PHP",clearable:""},model:{value:e.listQuery.php,callback:function(t){e.$set(e.listQuery,"php",t)},expression:"listQuery.php"}},e._l(e.phpOptions,function(e){return a("el-option",{key:e.key,attrs:{label:e.display_name,value:e.key}})}),1),e._v(" "),a("el-button",{directives:[{name:"waves",rawName:"v-waves"}],staticClass:"filter-item",attrs:{type:"primary",icon:"el-icon-search"},on:{click:e.handleFilter}},[e._v("\n      查找\n    ")]),e._v(" "),a("el-button",{staticClass:"filter-item",staticStyle:{"margin-left":"10px"},attrs:{type:"primary",icon:"el-icon-edit"},on:{click:e.handleCreate}},[e._v("\n      添加\n    ")])],1),e._v(" "),a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.listLoading,expression:"listLoading"}],key:e.tableKey,staticStyle:{width:"100%"},attrs:{data:e.list,border:"",fit:"","highlight-current-row":""},on:{"sort-change":e.sortChange}},[a("el-table-column",{attrs:{label:"ID",prop:"id",sortable:"custom",align:"center",width:"80","class-name":e.getSortClass("id")},scopedSlots:e._u([{key:"default",fn:function(t){return[a("span",[e._v(e._s(t.row.id))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Domain",prop:"domain",sortable:"custom","class-name":e.getSortClass("create_time"),"min-width":"150px"},scopedSlots:e._u([{key:"default",fn:function(t){var n=t.row;return[a("span",{staticClass:"link-type",on:{click:function(t){return e.handleUpdate(n)}}},[e._v(e._s(n.domain))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"PHP",width:"110px",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("span",[e._v(e._s(e._f("typeFilter")(t.row.php)))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"CreateDate",prop:"create_time",sortable:"custom","class-name":e.getSortClass("create_time"),width:"150px",align:"center"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("span",[e._v(e._s(e._f("parseTime")(t.row.create_time,"{y}-{m}-{d} {h}:{i}")))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"Actions",align:"center","min-width":"150px","class-name":"small-padding fixed-width"},scopedSlots:e._u([{key:"default",fn:function(t){var n=t.row;return[a("el-button",{attrs:{type:"primary",size:"mini"},on:{click:function(t){return e.handleUpdate(n)}}},[e._v("\n          编辑\n        ")]),e._v(" "),a("el-button",{attrs:{type:"success",size:"mini"},on:{click:function(t){return e.handleDomainList(n)}}},[e._v("\n          别名\n        ")]),e._v(" "),a("el-button",{attrs:{type:"warning",size:"mini"},on:{click:function(t){return e.handleProxyList(n)}}},[e._v("\n          反代\n        ")]),e._v(" "),"deleted"!=n.status?a("el-button",{attrs:{size:"mini",type:"danger"},on:{click:function(t){return e.handleDelete(n)}}},[e._v("\n          删除\n        ")]):e._e()]}}])})],1),e._v(" "),a("pagination",{directives:[{name:"show",rawName:"v-show",value:e.total>0,expression:"total>0"}],attrs:{total:e.total,page:e.listQuery.page,limit:e.listQuery.limit},on:{"update:page":function(t){return e.$set(e.listQuery,"page",t)},"update:limit":function(t){return e.$set(e.listQuery,"limit",t)},pagination:e.getList}}),e._v(" "),a("el-dialog",{attrs:{title:e.textMap[e.dialogStatus],visible:e.dialogFormVisible},on:{"update:visible":function(t){e.dialogFormVisible=t}}},[a("el-form",{ref:"dataForm",staticStyle:{width:"400px","margin-left":"50px"},attrs:{rules:e.rules,model:e.temp,"label-position":"left","label-width":"70px"}},[a("el-form-item",{attrs:{label:"主域名",prop:"domain"}},[a("el-input",{attrs:{placeholder:"请输入主要域名"},on:{change:e.handleDomainChange},model:{value:e.temp.domain,callback:function(t){e.$set(e.temp,"domain",t)},expression:"temp.domain"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"网站目录",prop:"root"}},[a("el-input",{attrs:{placeholder:"请输入网站目录"},model:{value:e.temp.root,callback:function(t){e.$set(e.temp,"root",t)},expression:"temp.root"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"管理员邮箱",prop:"email"}},[a("el-input",{attrs:{placeholder:"请输入管理员邮箱"},model:{value:e.temp.email,callback:function(t){e.$set(e.temp,"email",t)},expression:"temp.email"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"启用HTTPS"}},[a("el-select",{staticClass:"filter-item",attrs:{placeholder:"Please select"},model:{value:e.temp.autossl,callback:function(t){e.$set(e.temp,"autossl",t)},expression:"temp.autossl"}},e._l(e.statusOptions,function(e){return a("el-option",{key:e.key,attrs:{label:e.display_name,value:e.key}})}),1)],1),e._v(" "),a("el-form-item",{attrs:{label:"根证书",prop:"tls_chain"}},[a("el-input",{attrs:{placeholder:"请输入根证书文件路径"},model:{value:e.temp.tls_chain,callback:function(t){e.$set(e.temp,"tls_chain",t)},expression:"temp.tls_chain"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"证书",prop:"tls_crt"}},[a("el-input",{attrs:{placeholder:"请输入证书文件路径"},model:{value:e.temp.tls_crt,callback:function(t){e.$set(e.temp,"tls_crt",t)},expression:"temp.tls_crt"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"密钥",prop:"tls_key"}},[a("el-input",{attrs:{placeholder:"请输入密钥文件路径"},model:{value:e.temp.tls_key,callback:function(t){e.$set(e.temp,"tls_key",t)},expression:"temp.tls_key"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"GZIP"}},[a("el-select",{staticClass:"filter-item",attrs:{placeholder:"Please select"},model:{value:e.temp.gzip,callback:function(t){e.$set(e.temp,"gzip",t)},expression:"temp.gzip"}},e._l(e.statusOptions,function(e){return a("el-option",{key:e.key,attrs:{label:e.display_name,value:e.key}})}),1)],1),e._v(" "),a("el-form-item",{attrs:{label:"PHP",prop:"php"}},[a("el-select",{staticClass:"filter-item",attrs:{placeholder:"Please select"},model:{value:e.temp.php,callback:function(t){e.$set(e.temp,"php",t)},expression:"temp.php"}},e._l(e.phpOptions,function(e){return a("el-option",{key:e.key,attrs:{label:e.display_name,value:e.key}})}),1)],1),e._v(" "),a("el-form-item",{attrs:{label:"自定义配置"}},[a("el-input",{attrs:{autosize:{minRows:2,maxRows:4},type:"textarea",placeholder:"Please input"},model:{value:e.temp.customize,callback:function(t){e.$set(e.temp,"customize",t)},expression:"temp.customize"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"创建同名数据库",prop:"mysql"}},[a("el-select",{staticClass:"filter-item",attrs:{placeholder:"Please select"},model:{value:e.temp.mysql,callback:function(t){e.$set(e.temp,"mysql",t)},expression:"temp.mysql"}},e._l(e.mysqlOptions,function(e){return a("el-option",{key:e.key,attrs:{label:e.display_name,value:e.key}})}),1)],1)],1),e._v(" "),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.dialogFormVisible=!1}}},[e._v("\n        取消\n      ")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:function(t){"create"===e.dialogStatus?e.createData():e.updateData()}}},[e._v("\n        提交\n      ")])],1)],1),e._v(" "),a("el-dialog",{attrs:{visible:e.dialogPvVisible,title:"Reading statistics"},on:{"update:visible":function(t){e.dialogPvVisible=t}}},[a("el-table",{staticStyle:{width:"100%"},attrs:{data:e.pvData,border:"",fit:"","highlight-current-row":""}},[a("el-table-column",{attrs:{prop:"key",label:"Channel"}}),e._v(" "),a("el-table-column",{attrs:{prop:"pv",label:"Pv"}})],1),e._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{attrs:{type:"primary"},on:{click:function(t){e.dialogPvVisible=!1}}},[e._v("Confirm")])],1)],1)],1)},i=[],o=(a("ac4d"),a("8a81"),a("ac6a"),a("43f2")),s=a("6724"),l=a("ed08"),r=a("333d"),c=[{key:0,display_name:"静态"},{key:9056,display_name:"5.6"},{key:9073,display_name:"7.3"}],u=c.reduce(function(e,t){return e[t.key]=t.display_name,e},{}),p=[{key:0,display_name:"禁用"},{key:1,display_name:"启用"}],d=p.reduce(function(e,t){return e[t.key]=t.display_name,e},{}),m=[{key:0,display_name:"不创建"},{key:5,display_name:"创建Mysql5"},{key:8,display_name:"创建Mysql8"}],f={id:void 0,customize:"",domain:"",root:"",tls_crt:"",tls_key:"",php:0,gzip:1,autossl:0,mysql:5},h={name:"Vhosts",components:{Pagination:r["a"]},directives:{waves:s["a"]},filters:{statusFilter:function(e){return d[e]},typeFilter:function(e){return u[e]}},data:function(){return{tableKey:0,list:null,total:0,listLoading:!0,listQuery:{page:1,importance:void 0,domain:void 0,type:void 0,ordering:void 0},phpOptions:c,statusOptions:p,mysqlOptions:m,showReviewer:!1,temp:f,dialogFormVisible:!1,dialogStatus:"",textMap:{update:"Edit",create:"Create"},dialogPvVisible:!1,pvData:[],rules:{domain:[{required:!0,message:"domain is required",trigger:"blur"}],root:[{required:!0,message:"root is required",trigger:"blur"}]},downloadLoading:!1}},created:function(){this.getList()},methods:{getList:function(){var e=this;this.listLoading=!0,Object(o["g"])(this.listQuery).then(function(t){e.list=t.data.results,e.total=t.data.count,setTimeout(function(){e.listLoading=!1},1500)}).catch(function(e){return console.log(e)})},handleFilter:function(){this.listQuery.page=1,this.getList()},handleDomainChange:function(){""===this.temp.root&&(this.temp.root=this.temp.domain)},sortChange:function(e){var t=e.prop,a=e.order;this.listQuery.ordering="ascending"===a?"".concat(t):"-".concat(t),null==t&&(this.listQuery.ordering=""),console.log(t),this.handleFilter()},resetTemp:function(){this.temp=f},handleCreate:function(){var e=this;this.resetTemp(),this.dialogStatus="create",this.dialogFormVisible=!0,this.$nextTick(function(){e.$refs["dataForm"].clearValidate()})},createData:function(){var e=this;this.$refs["dataForm"].validate(function(t){t&&(e.temp.author="vue-element-admin",Object(o["c"])(e.temp).then(function(){e.list.unshift(e.temp),e.dialogFormVisible=!1,e.$notify({title:"Success",message:"创建成功",type:"success",duration:2e3}),e.getList()}))})},handleUpdate:function(e){var t=this;this.temp=Object.assign({},e),this.dialogStatus="update",this.dialogFormVisible=!0,this.$nextTick(function(){t.$refs["dataForm"].clearValidate()})},updateData:function(){var e=this;this.$refs["dataForm"].validate(function(t){if(t){var a=Object.assign({},e.temp);Object(o["l"])(a).then(function(){var t=!0,a=!1,n=void 0;try{for(var i,o=e.list[Symbol.iterator]();!(t=(i=o.next()).done);t=!0){var s=i.value;if(s.id===e.temp.id){var l=e.list.indexOf(s);e.list.splice(l,1,e.temp);break}}}catch(r){a=!0,n=r}finally{try{t||null==o.return||o.return()}finally{if(a)throw n}}e.dialogFormVisible=!1,e.$notify({title:"Success",message:"修改成功",type:"success",duration:2e3}),e.getList()})}})},handleDomainList:function(e){this.$router.push({path:"/vhosts/domain/".concat(e.id)})},handleProxyList:function(e){this.$router.push({path:"/vhosts/proxy/".concat(e.id)})},handleDelete:function(e){var t=this;console.log(e.id),Object(o["f"])(e.id).then(function(){t.$notify({title:"Success",message:"删除成功",type:"success",duration:2e3}),t.getList()})},formatJson:function(e,t){return t.map(function(t){return e.map(function(e){return"timestamp"===e?Object(l["f"])(t[e]):t[e]})})},getSortClass:function(e){var t=this.listQuery.ordering;return t==="".concat(e)?"ascending":t==="-".concat(e)?"descending":""}}},v=h,g=a("2877"),y=Object(g["a"])(v,n,i,!1,null,null,null);t["default"]=y.exports},e498:function(e,t,a){"use strict";var n=a("7456"),i=a.n(n);i.a}}]);