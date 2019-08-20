import request from '@/utils/request_api'
export function fetchList(query) {
  return request({
    url: '/plugins/list/',
    method: 'get',
    params: query,
    baseURL: process.env.VUE_APP_API_VERSION
  })
}
export function setup(query) {
  return request({
    url: '/plugins/list/setup/',
    method: 'get',
    params: query,
    baseURL: process.env.VUE_APP_API_VERSION
  })
}
export function remove(id) {
  return request({
    url: '/plugins/list/remove/',
    method: 'get',
    params: { id: id },
    baseURL: process.env.VUE_APP_API_VERSION
  })
}
export function restart(id) {
  return request({
    url: '/plugins/list/restart/',
    method: 'get',
    params: { id: id },
    baseURL: process.env.VUE_APP_API_VERSION
  })
}
