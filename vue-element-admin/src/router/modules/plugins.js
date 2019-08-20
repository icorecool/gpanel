/** When your routing table is too long, you can split it into small modules **/

import Layout from '@/layout'

const pluginsRouter = {
  path: '/plugins',
  component: Layout,
  redirect: '/plugins/list',
  name: 'Plugins',
  meta: {
    title: 'Plugins',
    icon: 'tree'
  },
  children: [
    {
      path: 'list',
      component: () => import('@/views/plugins/list'),
      name: 'Plugins List',
      meta: { title: 'Plugins List' }
    }
  ]
}
export default pluginsRouter
