(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-79481506"],{"333d":function(t,e,a){"use strict";var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"pagination-container",class:{hidden:t.hidden}},[a("el-pagination",t._b({attrs:{background:t.background,"current-page":t.currentPage,"page-size":t.pageSize,layout:t.layout,"page-sizes":t.pageSizes,total:t.total},on:{"update:currentPage":function(e){t.currentPage=e},"update:current-page":function(e){t.currentPage=e},"update:pageSize":function(e){t.pageSize=e},"update:page-size":function(e){t.pageSize=e},"size-change":t.handleSizeChange,"current-change":t.handleCurrentChange}},"el-pagination",t.$attrs,!1))],1)},i=[];a("c5f6");Math.easeInOutQuad=function(t,e,a,n){return t/=n/2,t<1?a/2*t*t+e:(t--,-a/2*(t*(t-2)-1)+e)};var o=function(){return window.requestAnimationFrame||window.webkitRequestAnimationFrame||window.mozRequestAnimationFrame||function(t){window.setTimeout(t,1e3/60)}}();function r(t){document.documentElement.scrollTop=t,document.body.parentNode.scrollTop=t,document.body.scrollTop=t}function s(){return document.documentElement.scrollTop||document.body.parentNode.scrollTop||document.body.scrollTop}function l(t,e,a){var n=s(),i=t-n,l=20,u=0;e="undefined"===typeof e?500:e;var c=function t(){u+=l;var s=Math.easeInOutQuad(u,n,i,e);r(s),u<e?o(t):a&&"function"===typeof a&&a()};c()}var u={name:"Pagination",props:{total:{required:!0,type:Number},page:{type:Number,default:1},limit:{type:Number,default:20},pageSizes:{type:Array,default:function(){return[10,20,30,50]}},layout:{type:String,default:"total, sizes, prev, pager, next, jumper"},background:{type:Boolean,default:!0},autoScroll:{type:Boolean,default:!0},hidden:{type:Boolean,default:!1}},computed:{currentPage:{get:function(){return this.page},set:function(t){this.$emit("update:page",t)}},pageSize:{get:function(){return this.limit},set:function(t){this.$emit("update:limit",t)}}},methods:{handleSizeChange:function(t){this.$emit("pagination",{page:this.currentPage,limit:t}),this.autoScroll&&l(0,800)},handleCurrentChange:function(t){this.$emit("pagination",{page:t,limit:this.pageSize}),this.autoScroll&&l(0,800)}}},c=u,d=(a("e498"),a("2877")),p=Object(d["a"])(c,n,i,!1,null,"6af373ef",null);e["a"]=p.exports},"43f2":function(t,e,a){"use strict";a.d(e,"g",function(){return i}),a.d(e,"c",function(){return o}),a.d(e,"l",function(){return r}),a.d(e,"f",function(){return s}),a.d(e,"h",function(){return l}),a.d(e,"a",function(){return u}),a.d(e,"j",function(){return c}),a.d(e,"d",function(){return d}),a.d(e,"i",function(){return p}),a.d(e,"b",function(){return m}),a.d(e,"k",function(){return f}),a.d(e,"e",function(){return h});var n=a("5a65");function i(t){return Object(n["a"])({url:"/vhosts/vhost/",method:"get",params:t,baseURL:"/v1"})}function o(t){return Object(n["a"])({url:"/vhosts/vhost/",method:"post",data:t,baseURL:"/v1"})}function r(t){return Object(n["a"])({url:"/vhosts/vhost/"+t.id+"/",method:"patch",data:t,baseURL:"/v1"})}function s(t){return Object(n["a"])({url:"/vhosts/vhost/"+t+"/",method:"delete",baseURL:"/v1"})}function l(t){return Object(n["a"])({url:"/vhosts/domain/",method:"get",params:t,baseURL:"/v1"})}function u(t){return Object(n["a"])({url:"/vhosts/domain/",method:"post",data:t,baseURL:"/v1"})}function c(t){return Object(n["a"])({url:"/vhosts/domain/"+t.id+"/",method:"patch",data:t,baseURL:"/v1"})}function d(t){return Object(n["a"])({url:"/vhosts/domain/"+t+"/",method:"delete",baseURL:"/v1"})}function p(t){return Object(n["a"])({url:"/vhosts/proxy/",method:"get",params:t,baseURL:"/v1"})}function m(t){return Object(n["a"])({url:"/vhosts/proxy/",method:"post",data:t,baseURL:"/v1"})}function f(t){return Object(n["a"])({url:"/vhosts/proxy/"+t.id+"/",method:"patch",data:t,baseURL:"/v1"})}function h(t){return Object(n["a"])({url:"/vhosts/proxy/"+t+"/",method:"delete",baseURL:"/v1"})}},"5a65":function(t,e,a){"use strict";a("6762");var n=a("bc3a"),i=a.n(n),o=a("5c96"),r=a("4360"),s=a("5f87");function l(t){var e=arguments.length>1&&void 0!==arguments[1]?arguments[1]:void 0,a=[200,201,204,400,410,422];return a.includes(t.status)?t:401===t.status?(o["MessageBox"].confirm("You have been logged out, you can cancel to stay on this page, or log in again","Confirm logout",{confirmButtonText:"Re-Login",cancelButtonText:"Cancel",type:"warning"}).then(function(){r["a"].dispatch("user/resetToken").then(function(){location.reload()})}),Promise.reject(new Error(t.data||"Error"))):(404===t.status&&Object(o["Message"])({message:"资源不存在,或已删除",type:"error",duration:5e3}),e.request?console.log(e.request):console.log("Error",e.message),Object(o["Message"])({message:e.message||"Error",type:"error",duration:5e3}),console.log("err"+e),Promise.reject(e))}var u=i.a.create({baseURL:"/v1",timeout:5e3});u.interceptors.request.use(function(t){return r["a"].getters.token&&(t.headers["X-Token"]=Object(s["a"])()),t},function(t){return console.log(t),Promise.reject(t)}),u.interceptors.response.use(function(t){return l(t)},function(t){return l(t.response,t)}),e["a"]=u},6724:function(t,e,a){"use strict";a("8d41");var n="@@wavesContext";function i(t,e){function a(a){var n=Object.assign({},e.value),i=Object.assign({ele:t,type:"hit",color:"rgba(0, 0, 0, 0.15)"},n),o=i.ele;if(o){o.style.position="relative",o.style.overflow="hidden";var r=o.getBoundingClientRect(),s=o.querySelector(".waves-ripple");switch(s?s.className="waves-ripple":(s=document.createElement("span"),s.className="waves-ripple",s.style.height=s.style.width=Math.max(r.width,r.height)+"px",o.appendChild(s)),i.type){case"center":s.style.top=r.height/2-s.offsetHeight/2+"px",s.style.left=r.width/2-s.offsetWidth/2+"px";break;default:s.style.top=(a.pageY-r.top-s.offsetHeight/2-document.documentElement.scrollTop||document.body.scrollTop)+"px",s.style.left=(a.pageX-r.left-s.offsetWidth/2-document.documentElement.scrollLeft||document.body.scrollLeft)+"px"}return s.style.backgroundColor=i.color,s.className="waves-ripple z-active",!1}}return t[n]?t[n].removeHandle=a:t[n]={removeHandle:a},a}var o={bind:function(t,e){t.addEventListener("click",i(t,e),!1)},update:function(t,e){t.removeEventListener("click",t[n].removeHandle,!1),t.addEventListener("click",i(t,e),!1)},unbind:function(t){t.removeEventListener("click",t[n].removeHandle,!1),t[n]=null,delete t[n]}},r=function(t){t.directive("waves",o)};window.Vue&&(window.waves=o,Vue.use(r)),o.install=r;e["a"]=o},7456:function(t,e,a){},"7f2a":function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"app-container"},[a("div",{staticClass:"filter-container"},[a("el-input",{staticClass:"filter-item",staticStyle:{width:"200px"},attrs:{placeholder:"请求路径"},nativeOn:{keyup:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.handleFilter(e)}},model:{value:t.listQuery.from_path,callback:function(e){t.$set(t.listQuery,"from_path",e)},expression:"listQuery.from_path"}}),t._v(" "),a("el-button",{directives:[{name:"waves",rawName:"v-waves"}],staticClass:"filter-item",attrs:{type:"primary",icon:"el-icon-search"},on:{click:t.handleFilter}},[t._v("\n      查找\n    ")]),t._v(" "),a("el-button",{staticClass:"filter-item",staticStyle:{"margin-left":"10px"},attrs:{type:"primary",icon:"el-icon-edit"},on:{click:t.handleCreate}},[t._v("\n      添加\n    ")])],1),t._v(" "),a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:t.listLoading,expression:"listLoading"}],key:t.tableKey,staticStyle:{width:"100%"},attrs:{data:t.list,border:"",fit:"","highlight-current-row":""},on:{"sort-change":t.sortChange}},[a("el-table-column",{attrs:{label:"ID",prop:"id",sortable:"custom",align:"center",width:"80","class-name":t.getSortClass("id")},scopedSlots:t._u([{key:"default",fn:function(e){return[a("span",[t._v(t._s(e.row.id))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"CreateDate",prop:"create_time",sortable:"custom","class-name":t.getSortClass("create_time"),width:"150px",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("span",[t._v(t._s(t._f("parseTime")(e.row.create_time,"{y}-{m}-{d} {h}:{i}")))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"请求路径",prop:"from_path",sortable:"custom","class-name":t.getSortClass("from_path"),"min-width":"150px"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("span",{staticClass:"link-type",on:{click:function(e){return t.handleUpdate(n)}}},[t._v(t._s(n.from_path))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"目标url",prop:"to_url",sortable:"custom","class-name":t.getSortClass("to_url"),"min-width":"150px"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("a",{staticClass:"target",attrs:{href:n.to_url,target:"_blank"}},[t._v(t._s(n.to_url))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"Actions",align:"center",width:"230","class-name":"small-padding fixed-width"},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.row;return[a("el-button",{attrs:{type:"primary",size:"mini"},on:{click:function(e){return t.handleUpdate(n)}}},[t._v("\n          编辑\n        ")]),t._v(" "),"deleted"!=n.status?a("el-button",{attrs:{size:"mini",type:"danger"},on:{click:function(e){return t.handleDelete(n)}}},[t._v("\n          删除\n        ")]):t._e()]}}])})],1),t._v(" "),a("pagination",{directives:[{name:"show",rawName:"v-show",value:t.total>0,expression:"total>0"}],attrs:{total:t.total,page:t.listQuery.page,limit:t.listQuery.limit},on:{"update:page":function(e){return t.$set(t.listQuery,"page",e)},"update:limit":function(e){return t.$set(t.listQuery,"limit",e)},pagination:t.getList}}),t._v(" "),a("el-dialog",{attrs:{title:t.textMap[t.dialogStatus],visible:t.dialogFormVisible},on:{"update:visible":function(e){t.dialogFormVisible=e}}},[a("el-form",{ref:"dataForm",staticStyle:{width:"400px","margin-left":"50px"},attrs:{rules:t.rules,model:t.temp,"label-position":"left","label-width":"70px"}},[a("el-form-item",{attrs:{label:"请求路径",prop:"from_path"}},[a("el-input",{attrs:{placeholder:"请输入请求路径"},model:{value:t.temp.from_path,callback:function(e){t.$set(t.temp,"from_path",e)},expression:"temp.from_path"}}),t._v(" "),a("el-input",{attrs:{type:"hidden",readonly:""},model:{value:t.temp.vhost,callback:function(e){t.$set(t.temp,"vhost",e)},expression:"temp.vhost"}})],1),t._v(" "),a("el-form-item",{attrs:{label:"目标url",prop:"to_url"}},[a("el-input",{attrs:{placeholder:"请输入目标url"},model:{value:t.temp.to_url,callback:function(e){t.$set(t.temp,"to_url",e)},expression:"temp.to_url"}})],1),t._v(" "),a("el-form-item",{attrs:{label:"websocket"}},[a("el-select",{staticClass:"filter-item",attrs:{placeholder:"Please select"},model:{value:t.temp.websocket,callback:function(e){t.$set(t.temp,"websocket",e)},expression:"temp.websocket"}},t._l(t.statusOptions,function(t){return a("el-option",{key:t.key,attrs:{label:t.display_name,value:t.key}})}),1)],1),t._v(" "),a("el-form-item",{attrs:{label:"排除字符串",prop:"without"}},[a("el-input",{attrs:{placeholder:"请输入排除字符串"},model:{value:t.temp.without,callback:function(e){t.$set(t.temp,"without",e)},expression:"temp.without"}})],1)],1),t._v(" "),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(e){t.dialogFormVisible=!1}}},[t._v("\n        取消\n      ")]),t._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:function(e){"create"===t.dialogStatus?t.createData():t.updateData()}}},[t._v("\n        提交\n      ")])],1)],1),t._v(" "),a("el-dialog",{attrs:{visible:t.dialogPvVisible,title:"Reading statistics"},on:{"update:visible":function(e){t.dialogPvVisible=e}}},[a("el-table",{staticStyle:{width:"100%"},attrs:{data:t.pvData,border:"",fit:"","highlight-current-row":""}},[a("el-table-column",{attrs:{prop:"key",label:"Channel"}}),t._v(" "),a("el-table-column",{attrs:{prop:"pv",label:"Pv"}})],1),t._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{attrs:{type:"primary"},on:{click:function(e){t.dialogPvVisible=!1}}},[t._v("Confirm")])],1)],1)],1)},i=[],o=(a("ac4d"),a("8a81"),a("ac6a"),a("43f2")),r=a("6724"),s=a("333d"),l=[{key:0,display_name:"禁用"},{key:1,display_name:"启用"}],u=l.reduce(function(t,e){return t[e.key]=e.display_name,t},{}),c={id:void 0,from_path:"",to_url:"",websocket:0,with_out:"",vhost:0},d={name:"Proxy",components:{Pagination:s["a"]},directives:{waves:r["a"]},filters:{statusFilter:function(t){return u[t]}},data:function(){return{tableKey:0,list:null,total:0,listLoading:!0,listQuery:{page:1,vhost:this.$route.params.id,from_path:void 0,ordering:void 0},statusOptions:l,showReviewer:!1,temp:c,dialogFormVisible:!1,dialogStatus:"",textMap:{update:"Edit",create:"Create"},dialogPvVisible:!1,pvData:[],rules:{domain:[{required:!0,message:"domain is required",trigger:"change"}],timestamp:[{type:"date",required:!0,message:"timestamp is required",trigger:"change"}],title:[{required:!0,message:"title is required",trigger:"blur"}]},downloadLoading:!1}},created:function(){this.getList()},methods:{getList:function(){var t=this;this.listLoading=!0,this.temp.vhost=this.$route.params.id,Object(o["i"])(this.listQuery).then(function(e){t.list=e.data.results,t.total=e.data.count,setTimeout(function(){t.listLoading=!1},1500)}).catch(function(t){return console.log(t)})},handleFilter:function(){this.listQuery.page=1,this.getList()},handleDomainChange:function(){""===this.temp.root&&(this.temp.root=this.temp.domain)},sortChange:function(t){var e=t.prop,a=t.order;this.listQuery.ordering="ascending"===a?"".concat(e):"-".concat(e),null==e&&(this.listQuery.ordering=""),console.log(e),this.handleFilter()},resetTemp:function(){this.temp=c},handleCreate:function(){var t=this;this.resetTemp(),this.dialogStatus="create",this.dialogFormVisible=!0,this.$nextTick(function(){t.$refs["dataForm"].clearValidate()})},createData:function(){var t=this;this.$refs["dataForm"].validate(function(e){e&&(t.temp.author="vue-element-admin",Object(o["b"])(t.temp).then(function(){t.list.unshift(t.temp),t.dialogFormVisible=!1,t.$notify({title:"Success",message:"创建成功",type:"success",duration:2e3}),t.getList()}))})},handleUpdate:function(t){var e=this;this.temp=Object.assign({},t),this.dialogStatus="update",this.dialogFormVisible=!0,this.$nextTick(function(){e.$refs["dataForm"].clearValidate()})},updateData:function(){var t=this;this.$refs["dataForm"].validate(function(e){if(e){var a=Object.assign({},t.temp);Object(o["k"])(a).then(function(){var e=!0,a=!1,n=void 0;try{for(var i,o=t.list[Symbol.iterator]();!(e=(i=o.next()).done);e=!0){var r=i.value;if(r.id===t.temp.id){var s=t.list.indexOf(r);t.list.splice(s,1,t.temp);break}}}catch(l){a=!0,n=l}finally{try{e||null==o.return||o.return()}finally{if(a)throw n}}t.dialogFormVisible=!1,t.$notify({title:"Success",message:"修改成功",type:"success",duration:2e3}),t.getList()})}})},handleDelete:function(t){var e=this;console.log(t.id),Object(o["e"])(t.id).then(function(){e.$notify({title:"Success",message:"删除成功",type:"success",duration:2e3}),e.getList()})},getSortClass:function(t){var e=this.listQuery.ordering;return e==="".concat(t)?"ascending":e==="-".concat(t)?"descending":""}}},p=d,m=a("2877"),f=Object(m["a"])(p,n,i,!1,null,null,null);e["default"]=f.exports},"8d41":function(t,e,a){},e498:function(t,e,a){"use strict";var n=a("7456"),i=a.n(n);i.a}}]);