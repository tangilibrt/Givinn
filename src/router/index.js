import { createWebHistory, createRouter } from "vue-router";
import HomeView from "@/components/Home/HomeView.vue";
import ConcoursView from "@/components/Concours/ConcoursView.vue";
import SoloConcoursView from "@/components/Concours/DetailsConcours/SoloConcoursView.vue";
import WhoView from "@/components/Who/WhoView.vue";

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
    },
    {
        path: '/QuiSommesNous',
        name: 'QuiSommesNous',
        component: WhoView
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes
})

export default router