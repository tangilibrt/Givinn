<template>
  <div class="container">
    <h1>Concours</h1>

    <div class="search" style="position: absolute; top: 200px">
      <input type="text" v-model="searchQuery" placeholder="Rechercher un concours">
    </div>
    <menu class="sort">
      <li>
        <button @click="sorting('endDateAsc')">Par date de fin croissante</button>
      </li>
      <li>
        <button @click="sorting('endDateDesc')">Par date de fin décroissante</button>
      </li>
      <li>
        <button @click="sorting('confidenceAsc')">Par indice de confiance croissant</button>
      </li>
      <li>
        <button @click="sorting('confidenceDesc')">Par indice de confiance décroissant</button>
      </li>
    </menu>
    <div class="cursorLine"></div>
    <div class="line"/>
    <div class="cardContainer">
      <div v-for="concours in sortedConcours" v-bind:key="concours.id">
        <ConcoursCard :concours=concours />
      </div>
    </div>
  </div>
</template>

<script>
import ConcoursCard from "@/components/Concours/ConcoursCard.vue";
import informations from "/src/Python/venv/Scripts/db/concours.json";

export default {
  name: "ConcoursView",
  components: {ConcoursCard},
  data() {
    return {
      informations,
      searchQuery: '',
      sortBy: '',
    };
  },
  computed: {
    filteredConcours() {
      if (this.searchQuery) {
        const query = this.searchQuery.toLowerCase();
        return Object.values(this.informations.concours).filter((concours) => {
          return concours.caption.toLowerCase().includes(query);
        })
      } else {
        return this.informations.concours;
      }
    },
    sortedConcours() {
      const cursorLine = document.querySelector('.cursorLine');

      if (this.sortBy === 'endDateAsc') {
        cursorLine.style.top = '240px';
        return Object.values(this.filteredConcours).sort((a, b) => {
          const dateA = new Date(a.end_date);
          const dateB = new Date(b.end_date);
          return dateA - dateB;
        });
      } else if (this.sortBy === 'endDateDesc') {
        cursorLine.style.top = '325px';
        return Object.values(this.filteredConcours).sort((a, b) => {
          const dateA = new Date(a.end_date);
          const dateB = new Date(b.end_date);
          return dateB - dateA;
        });
      } else if (this.sortBy === 'confidenceAsc') {
        cursorLine.style.top = '406px';
        return Object.values(this.filteredConcours).sort((a, b) => {
          return a.confidence - b.confidence;
        });
      } else if (this.sortBy === 'confidenceDesc') {
        cursorLine.style.top = '486px';
        return Object.values(this.filteredConcours).sort((a, b) => {
          return b.confidence - a.confidence;
        });
      } else {
        return Object.values(this.filteredConcours).sort((a, b) => {
          const dateA = new Date(a.end_date);
          const dateB = new Date(b.end_date);
          return dateA - dateB;
        });
      }
    },
  },
  methods: {
    sorting(method) {
      this.sortBy = method;
    },

  }
}
</script>

<style scoped lang="scss">
.cardContainer {
  position: relative;
  height: 300px;
  width: 80%;
  top: 200px;
  display: flex;
  flex-flow: row wrap;
  justify-content: center;
  transform: translate(-50%, 50%);
  left: 50%;
}

.container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.search {
  position: relative;
  top: 200px;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 40%;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.search input {
  width: 100%;
  height: 100%;
  border: none;
  outline: none;
  font-size: 1.2rem;
  padding-left: 10px;
  border-radius: 10px;
  text-align: center;
}

.sort {
  position: absolute;
  top: 200px;
  left: 85%;
  transition: 0.5s;
  width: 10vw;
  height: auto;
  display: flex;
  flex-flow: column;
  justify-content: flex-start;
  border-left: 1px solid lightgrey;

  :nth-child(n+1) {
    border-top: 1px solid lightgrey;
  }

  :first-child {
    border-top: none;
  }

  li {
    list-style: none;
    margin: 5px;

    button {
      width: 100%;
      height: 70px;
      border: none;
      outline: none;
      font-size: 1.2rem;
      padding-left: 10px;
      text-align: center;
      background-color: #fff;
      transition: 0.5s;

      &:hover {
        background-color: #f3f3f3;
        cursor: pointer;
      }
    }
  }
}

.cursorLine {
  position: absolute;
  top: 240px;
  left: 85.2%;
  transform: translate(-50%, -50%);
  width: 5px;
  height: 80px;
  background: linear-gradient(45deg, #405de6, #5851db, #833ab4, #c13584, #e1306c, #fd1d1d);
  transition: top 0.2s;
}

.line {
  position: absolute;
  top: 300px;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 30%;
  height: 1px;
  background-color: lightgrey;
}

h1 {
  color: black;
  position: absolute;
  top: 0;
  left: 50%;
  transform: translate(-50%, 50%);
  font-size: 50px;
}

@media screen and (max-width: 1450px){
    .sort {
      position: absolute;
      flex-flow: row;
      left: 25%;
      transform: translate(50%, -50%);
      border-left: none;
      top: 300px;
      :nth-child(n+1) {
        border-top: none;
        border-left: 1px solid lightgrey;
      }
    }
    .cursorLine {
      opacity: 0;
    }
    .line {
      top: 380px;
    }
    .cardContainer {
      top: 300px;
    }
}

@media screen and (max-width: 470px){
    h1 {
      font-size: 40px;
    }
    .search {
      width: 80%;
    }
    .sort {
      max-width: 80%;
      left: 0%;
      li {
        button {
          font-size: .75rem;
        }
      }
    }
}

</style>