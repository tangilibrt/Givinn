<template>
  <div class = container>
    <h1>Accueil</h1>


    <section class="introduction">
      <who-title infos="Giv'inn"></who-title>
      <p>
        notre but, vous faire découvrir les concours les plus intéressants et les plus fiables disponible sur instagram
      </p>
    </section>
    <section class="giveAwayList">
      <who-title infos="comment ça marche ?"></who-title>
      <p>
        nous avons mis en place un système de notation des concours, plus l'indice de confiance est élevé, plus le concours est fiable
        comme par exemple:
      </p>
      <ul>
        <li>si le compte est certifié</li>
        <li>si le concours est organisé par une marque</li>
        <li>si le compte possède un grand nombre d'abonnés</li>
        <li>ce qui permet de participer au concours</li>
        <li>la date de début et de fin du concours</li>
      </ul>
    </section>
    <section>
      <who-title infos="les meilleurs concours"></who-title>
      <P>voici ci-dessous les 3 conocurs jugés les plus fiables</P>
      <div class="cardContainer">
        <div v-for="concours in descConcours" v-bind:key="concours.id">
          <ConcoursCard :concours=concours />
        </div>
      </div>
    </section>
  </div>

</template>

<script>
import WhoTitle from "@/components/Home/Titles.vue";
import ConcoursCard from "@/components/Concours/ConcoursCard.vue";
import informations from "/src/Python/venv/Scripts/db/concours.json";

export default {
  name: "HomeView",
  components: {ConcoursCard, WhoTitle},
  data() {
    return {
      informations,
      limit: 3,
    };
  },
  computed: {
    descConcours() {
      const giveAway = Object.values(this.informations.concours).sort((a, b) => {
        return b.confidence - a.confidence;
      });
      return giveAway.slice(0, this.limit);
    }
  }
}
</script>

<style scoped lang="scss">
  .container {
    margin: 0 auto;
    width: 80%;
    text-align: center;
    font-family: Inter, sans-serif;
    font-size: larger;

      section {
        color: #17141d;
      }

      li{
        text-align: justify;
        margin: 10px;
        font-size: medium;
        position: relative;
        left: 50%;
        transform: translateX(-50%);
      }

      p {
        margin: 20px 0;
        color: black;
      }

      h1 {
        color: black;
        text-align: center;
        font-size: 50px;
        top: 30px;
        left: auto;
      }
    .cardContainer {
      position: relative;
      display: flex;
      height: 300px;
      width: 80%;
      top: 100px;
      flex-flow: row wrap;
      justify-content: space-around;
      left: 50%;
      transform: translateX(-50%)scale(1.3);
    }
  }
</style>