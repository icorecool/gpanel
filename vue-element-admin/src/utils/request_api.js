import axios from 'axios'
import { MessageBox, Message } from 'element-ui'
import store from '@/store'
import { getToken } from '@/utils/auth'
function returnMessage(response, error = undefined) {
  const codeList = [200, 201, 204, 400, 410, 422]
  // 内容传回页面
  if (codeList.includes(response.status)) {
    return response
  }
  // 401没有权限
  if (response.status === 401) {
    // to re-login
    MessageBox.confirm('You have been logged out, you can cancel to stay on this page, or log in again', 'Confirm logout', {
      confirmButtonText: 'Re-Login',
      cancelButtonText: 'Cancel',
      type: 'warning'
    }).then(() => {
      store.dispatch('user/resetToken').then(() => {
        location.reload()
      })
    })
    return Promise.reject(new Error(response.data || 'Error'))
  }
  if (response.status === 404) {
    Message({
      message: '资源不存在,或已删除',
      type: 'error',
      duration: 5 * 1000
    })
  }
  // 错误处理
  if (error.request) {
    // The request was made but no response was received
    // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
    // http.ClientRequest in node.js
    console.log(error.request)
    // Message({
    //   message: error.request || 'Error',
    //   type: 'error',
    //   duration: 5 * 1000
    // })
  } else {
    // Something happened in setting up the request that triggered an Error
    console.log('Error', error.message)
  }
  Message({
    message: error.message || 'Error',
    type: 'error',
    duration: 5 * 1000
  })
  console.log('err' + error) // for debug
  return Promise.reject(error)
}
// create an axios instance
const service = axios.create({
  baseURL: process.env.VUE_APP_API_VERSION, // url = base url + request url
  // withCredentials: true, // send cookies when cross-domain requests
  timeout: 5000 // request timeout
})
// request interceptor
service.interceptors.request.use(
  config => {
    // do something before request is sent

    if (store.getters.token) {
      // let each request carry token
      // ['X-Token'] is a custom headers key
      // please modify it according to the actual situation
      config.headers['X-Token'] = getToken()
    }
    return config
  },
  error => {
    // do something with request error
    console.log(error) // for debug
    return Promise.reject(error)
  }
)

// response interceptor
service.interceptors.response.use(
  /**
   * If you want to get http information such as headers or status
   * Please return  response => response
  */

  /**
   * Determine the request status by custom code
   * Here is just an example
   * You can also judge the status by HTTP Status Code
   */
  response => {
    return returnMessage(response)
  },
  error => {
    return returnMessage(error.response, error)
  }
)

export default service
