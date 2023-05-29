import { createWebHistory, createRouter } from "vue-router";
import HomeView from "@/components/Home/HomeView.vue";
import ConcoursView from "@/components/Concours/ConcoursView.vue";
import SoloConcoursView from "@/components/Concours/DetailsConcours/SoloConcoursView.vue";

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/concours',
        name: 'concours',
        component: ConcoursView,
    },
    {
        path: '/concours/:id',
        name: 'concours detail',
        component: SoloConcoursView
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes
})

export default router