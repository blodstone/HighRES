/**
 * Router configuration.
 */
import Vue from 'vue';
import Router from 'vue-router';
import Home from './components/admin/Home.vue';
import Admin from './views/admin/Admin.vue';
import NewProject from './components/admin/ProjectMenu/NewProject.vue';
import NewEvaluation from './components/admin/ProjectMenu/NewEvaluation.vue';
import EvalFluency from './views/user/EvalFluency.vue';

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
      path: '/admin',
      component: Admin,
      children: [
        {
          path: '',
          name: 'admin',
          component: Home,
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
    },
  ],
});
