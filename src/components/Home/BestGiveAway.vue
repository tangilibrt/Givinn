<template>
  <div v-for="concours in descConcours" v-bind:key="concours.id">
    <ConcoursCard :concours=concours />
  </div>
</template>

<script>
import ConcoursCard from "@/components/Concours/ConcoursCard.vue";
export default {
  name: "BestGiveAway",
  components: { ConcoursCard },
  computed: {
    descConcours() {
      const sortedConcours = Object.values(this.filteredConcours).sort((a, b) => {
        return b.confidence - a.confidence;
      });

      return sortedConcours.slice(0, this.limit);
    }
  }
}

</script>

