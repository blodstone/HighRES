/**
 * Router configuration.
 */
import Vue from 'vue';
import Router from 'vue-router';
import Home from './components/admin/Home.vue';
import Admin from './views/admin/Admin.vue';
import NewProject from './components/admin/ProjectMenu/NewProject.vue';
import NewEvaluation from './components/admin/ProjectMenu/NewEvaluation.vue';
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
//# sourceMappingURL=router.js.map