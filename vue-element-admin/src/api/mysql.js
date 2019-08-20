import request from '@/utils/request_api'
export function fetchList(query) {
  return request({
    url: '/mysql/list/',
    method: 'get',
    params: query,
    baseURL: process.env.VUE_APP_API_VERSION
  })
}
export function setup(query) {
  return request({
    url: '/mysql/list/createdb/',
    method: 'get',
    params: query,
    baseURL: process.env.VUE_APP_API_VERSION
  })
}
export function remove(id) {
  return request({
    url: '/mysql/list/removedb/',
    method: 'get',
    params: { id: id },
    baseURL: process.env.VUE_APP_API_VERSION
  })
}
