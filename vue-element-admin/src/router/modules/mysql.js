/** When your routing table is too long, you can split it into small modules **/

import Layout from '@/layout'

const mysqlRouter = {
  path: '/mysql',
  component: Layout,
  redirect: '/mysql/list',
  name: 'Mysql',
  meta: {
    title: 'Mysql',
    icon: 'tree'
  },
  children: [
    {
      path: 'list',
      component: () => import('@/views/mysql/list'),
      name: 'Mysql List',
      meta: { title: 'Mysql List' }
    }
  ]
}
export default mysqlRouter
