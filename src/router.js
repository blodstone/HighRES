/**
 * Router configuration.
 */
import Vue from 'vue';
import Router from 'vue-router';
import Home from './components/admin/Home.vue';
import Admin from './views/admin/Admin.vue';
import Login from './views/admin/Login.vue';
import ManageProject from './views/admin/ManageProject.vue';
import NewProject from './components/admin/ProjectMenu/NewProject.vue';
import NewEvaluation from './components/admin/ProjectMenu/NewEvaluation.vue';
import EvalClarity from './views/user/EvalClarity.vue';
import EvalFluency from './views/user/EvalFluency.vue';
import store from './store';

Vue.use(Router);
export default new Router({
  routes: [
    {
      path: '/',
      redirect: {
        name: 'admin',
      },
    },
    {
      path: '/fluency/:project_id/',
      name: 'fluency',
      component: EvalFluency,
    },
    {
      path: '/clarity/:project_id/',
      name: 'clarity',
      component: EvalClarity,
    },
    {
      path: '/admin',
      component: Admin,
      children: [
        {
          path: '',
          name: 'admin',
          component: Home,
        },
        {
          path: 'manage',
          name: 'manage',
          component: ManageProject,
        },
        {
          path: 'new',
          component: NewProject,
          children: [
            {
              path: '',
              name: 'new',
              component: NewEvaluation,
            },
            {
              path: 'evaluation',
              name: 'newEvaluation',
              component: NewEvaluation,
            },
          ],
        },
      ],
      beforeEnter(to, from, next) {
        if (!store.getters.isAuthenticated) {
          next('/login');
        } else {
          next();
        }
      },
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      beforeEnter(to, from, next) {
        if (store.getters.isAuthenticated) {
          next('/admin');
        } else {
          next();
        }
      },
    },
  ],
});
