import request from '@/utils/request_api'
// vhost
export function fetchList(query) {
  return request({
    url: '/caddy/vhost/',
    method: 'get',
    params: query,
    baseURL: process.env.VUE_APP_API_VERSION
  })
}

export function createVhost(data) {
  return request({
    url: '/caddy/vhost/',
    method: 'post',
    data,
    baseURL: process.env.VUE_APP_API_VERSION
  })
}

export function updateVhost(data) {
  return request({
    url: '/caddy/vhost/' + data.id + '/',
    method: 'patch',
    data,
    baseURL: process.env.VUE_APP_API_VERSION
  })
}
export function deleteVhost(id) {
  return request({
    url: '/caddy/vhost/' + id + '/',
    method: 'delete',
    baseURL: process.env.VUE_APP_API_VERSION
  })
}
// domain
export function listDomain(query) {
  return request({
    url: '/caddy/domain/',
    method: 'get',
    params: query,
    baseURL: process.env.VUE_APP_API_VERSION
  })
}

export function createDomain(data) {
  return request({
    url: '/caddy/domain/',
    method: 'post',
    data,
    baseURL: process.env.VUE_APP_API_VERSION
  })
}

export function updateDomain(data) {
  return request({
    url: '/caddy/domain/' + data.id + '/',
    method: 'patch',
    data,
    baseURL: process.env.VUE_APP_API_VERSION
  })
}
export function deleteDomain(id) {
  return request({
    url: '/caddy/domain/' + id + '/',
    method: 'delete',
    baseURL: process.env.VUE_APP_API_VERSION
  })
}
// proxy
export function listProxy(query) {
  return request({
    url: '/caddy/proxy/',
    method: 'get',
    params: query,
    baseURL: process.env.VUE_APP_API_VERSION
  })
}

export function createProxy(data) {
  return request({
    url: '/caddy/proxy/',
    method: 'post',
    data,
    baseURL: process.env.VUE_APP_API_VERSION
  })
}

export function updateProxy(data) {
  return request({
    url: '/caddy/proxy/' + data.id + '/',
    method: 'patch',
    data,
    baseURL: process.env.VUE_APP_API_VERSION
  })
}
export function deleteProxy(id) {
  return request({
    url: '/caddy/proxy/' + id + '/',
    method: 'delete',
    baseURL: process.env.VUE_APP_API_VERSION
  })
}
