<template>
  <div class = container>
    <section class="introduction">
      <Title infos="Giv'inn"></Title>
      <p>
        Notre but, vous faire découvrir les concours les plus intéressants et les plus fiables disponible sur Instagram
      </p>
    </section>
    <section class="giveAwayList">
      <who-title infos="comment ça marche ?"></who-title>
      <p>
        Nous avons mis en place un système de notation des concours, plus l'indice de confiance est élevé, plus le concours est fiable
        comme par exemple:
      </p>
      <ul>
        <li>Si le compte est certifié</li>
        <li>Si le concours est organisé par une marque</li>
        <li>Si le compte possède un grand nombre d'abonnés</li>
        <li>Ce qui permet de participer au concours</li>
        <li>La date de début et de fin du concours</li>
      </ul>
    </section>
    <section>
      <WhoTitle infos="les meilleurs concours"></WhoTitle>
      <P>Voici ci-dessous les 3 concours jugés les plus fiables</P>
      <div class="cardContainer">
        <div v-for="concours in descConcours" v-bind:key="concours.id">
          <ConcoursCard :concours=concours />
        </div>
      </div>
    </section>
  </div>

</template>

<script>
import Title from "@/components/Home/Titles.vue";
import WhoTitle from "@/components/Who/WhoTitle.vue";
import ConcoursCard from "@/components/Concours/ConcoursCard.vue";
import informations from "/src/Python/venv/Scripts/db/concours.json";

export default {
  name: "HomeView",
  components: {ConcoursCard, Title, WhoTitle},
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
      ul {
        li{
          list-style-type: none;
          text-align: justify;
          margin: 10px;
          font-size: medium;
          position: relative;
          left: 50%;
          transform: translateX(-50%);
        }
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
