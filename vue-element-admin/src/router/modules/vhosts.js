/** When your routing table is too long, you can split it into small modules **/

import Layout from '@/layout'

const vhostsRouter = {
  path: '/vhosts',
  component: Layout,
  redirect: '/vhosts/list',
  name: 'Vhosts',
  meta: {
    title: 'Vhosts',
    icon: 'tree'
  },
  children: [
    {
      path: 'list',
      component: () => import('@/views/vhosts/list'),
      name: 'Vhosts List',
      meta: { title: 'Vhosts List' }
    },
    {
      path: 'domain/:id(\\d+)',
      component: () => import('@/views/vhosts/domain'),
      name: 'Vhosts Domain List',
      meta: { title: 'Vhosts Domain List' },
      hidden: true
    },
    {
      path: 'proxy/:id(\\d+)',
      component: () => import('@/views/vhosts/proxy'),
      name: 'Vhosts Proxy List',
      meta: { title: 'Vhosts Proxy List' },
      hidden: true
    }
  ]
}
export default vhostsRouter
