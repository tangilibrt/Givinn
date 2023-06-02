<template>
  <div class="containerDetail">
    <div class="infos">
      <h1 class="twelve"> Concours de @{{ $route.params.id }}</h1>
      <div class="sub">
        <img :src='getImageUrl' class="image" alt="pfp"/>
        <div class="line">

        </div>
      </div>
      <div style="display: flex;flex-flow: row wrap;justify-content: center;align-items: center;">
        <div class="details">
          <div class="detail">
            <SoloConcoursInfoBlocNoir :infos="'Date de début: ' + informations.concours[$route.params.id]['date']"/>
          </div>
          <div class="detail">
            <SoloConcoursInfoBlocBlanc :infos="'Date de fin : ' + informations.concours[$route.params.id]['end_date']"/>
          </div>
          <div class="detail">
            <SoloConcoursInfoBlocNoir infos="Lien du concours "
                                      :link="informations.concours[$route.params.id]['url']"></SoloConcoursInfoBlocNoir>
          </div>
        </div>
        <div class="circle">
          <div id="circle_wave">
            <svg width="750" height="75" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"
                 version="1.1" xml:space="preserve">
             <g class="layer">
              <title>Layer 1</title>
               <g id="SVGRepo_bgCarrier" stroke-width="0"/>
               <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
               <g id="SVGRepo_iconCarrier">
               <g id="svg_1">
                <path
                    d="m63.42,51.11c8.82,-8.82 23.17,-8.82 31.99,0c24.42,24.42 64.15,24.42 88.56,0c4.28,-4.27 9.96,-6.62 16,-6.62s11.72,2.35 16,6.62c24.41,24.42 64.14,24.42 88.56,0c4.27,-4.27 9.95,-6.62 16,-6.62s11.72,2.35 15.99,6.62c11.83,11.83 27.56,18.34 44.28,18.34c16.73,0 32.46,-6.51 44.28,-18.34c7.81,-7.81 7.81,-20.47 0,-28.28c-7.81,-7.81 -20.47,-7.81 -28.28,0c-4.27,4.27 -9.95,6.63 -16,6.63s-11.72,-2.36 -15.99,-6.63c-11.83,-11.83 -27.56,-18.34 -44.28,-18.34c0,0 0,0 0,0c-16.73,0 -32.46,6.51 -44.28,18.34c-8.82,8.82 -23.18,8.82 -32,0c-11.82,-11.83 -27.55,-18.34 -44.28,-18.34c0,0 0,0 0,0c-16.72,0 -32.45,6.51 -44.28,18.34c-8.82,8.82 -23.17,8.82 -31.99,0c-24.42,-24.42 -64.15,-24.42 -88.56,0c-8.82,8.82 -23.17,8.82 -32,0c-7.81,-7.81 -20.47,-7.81 -28.28,0s-7.81,20.47 0,28.28c24.41,24.42 64.14,24.42 88.56,0z"
                    fill="#ff0000" id="svg_2"/>
               </g>
              </g>
               <g id="svg_3">
               <g id="svg_4">
                <path
                    d="m424.71,51.34c8.82,-8.82 23.17,-8.82 31.99,0c24.42,24.42 64.15,24.42 88.56,0c4.28,-4.27 9.96,-6.62 16,-6.62s11.72,2.35 16,6.62c24.41,24.42 64.14,24.42 88.56,0c4.27,-4.27 9.95,-6.62 16,-6.62s11.72,2.35 15.99,6.62c11.83,11.83 27.56,18.34 44.28,18.34c16.73,0 32.46,-6.51 44.28,-18.34c7.81,-7.81 7.81,-20.47 0,-28.28c-7.81,-7.81 -20.47,-7.81 -28.28,0c-4.27,4.27 -9.95,6.63 -16,6.63s-11.72,-2.36 -15.99,-6.63c-11.83,-11.83 -27.56,-18.34 -44.28,-18.34c0,0 0,0 0,0c-16.73,0 -32.46,6.51 -44.28,18.34c-8.82,8.82 -23.18,8.82 -32,0c-11.82,-11.83 -27.55,-18.34 -44.28,-18.34c0,0 0,0 0,0c-16.72,0 -32.45,6.51 -44.28,18.34c-8.82,8.82 -23.17,8.82 -31.99,0c-24.42,-24.42 -64.15,-24.42 -88.56,0c-8.82,8.82 -23.17,8.82 -32,0c-7.81,-7.81 -20.47,-7.81 -28.28,0s-7.81,20.47 0,28.28c24.41,24.42 64.14,24.42 88.56,0z"
                    fill="#ff0000" id="svg_5"/>
               </g>
              </g>
             </g>
            </svg>
          </div>
          <div id="circleLevel">
          </div>
          <a>{{ informations.concours[$route.params.id].confidence }}</a>

        </div>
      </div>
      <solo-concours-info-bloc-blanc
          class="description"
          :infos="informations.concours[$route.params.id].caption"></solo-concours-info-bloc-blanc>
    </div>
  </div>
</template>

<script>
import informations from "/src/Python/venv/Scripts/db/concours.json";
import SoloConcoursInfoBlocNoir from "@/components/Concours/DetailsConcours/SoloConcoursInfoBlocNoir.vue";
import SoloConcoursInfoBlocBlanc from "@/components/Concours/DetailsConcours/SoloConcoursInfoBlocBlanc.vue";

export default {
  name: "SoloConcoursView",
  components: {SoloConcoursInfoBlocBlanc, SoloConcoursInfoBlocNoir},

  data() {
    return {
      informations
    };
  },
  methods: {
    setCircleLevel(level) {
      const circleLevelElement = document.getElementById('circleLevel');
      const wave = document.getElementById('circle_wave');
      const maxHeight = 200; // Maximum height of the level (circle height)

      // Calculate the height based on the level (0 to 100)
      const height = (level / 100) * maxHeight;

      // Set the height of the water level element
      circleLevelElement.style.height = height + 'px';
      wave.style.bottom = -60 + height + 'px';
    },
    detColor(confidence) {
      const circleLevelElement = document.getElementById('circleLevel');
      const svg = document.getElementById('svg_2');
      const svg2 = document.getElementById('svg_5');
      if (confidence < 25) {
        console.log("red");
        circleLevelElement.style.background = "red";
        svg.style.fill = "red";
        svg2.style.fill = "red";
      } else if (confidence < 50) {
        console.log("orange");
        circleLevelElement.style.background = "orange";
        svg.style.fill = "orange";
        svg2.style.fill = "orange";
      } else if (confidence < 75) {
        console.log("yellow");
        circleLevelElement.style.background = "yellow";
        svg.style.fill = "yellow";
        svg2.style.fill = "yellow";
      } else if (confidence < 100) {
        console.log("green");
        circleLevelElement.style.background = "green";
        svg.style.fill = "green";
        svg2.style.fill = "green";
      }
    },
  },
  mounted() {
    const confidence = this.informations.concours[this.$route.params.id].intConfidence;
    this.setCircleLevel(confidence);
    this.detColor(confidence);

  },
  computed: {
    getImageUrl() {
      // if image exist : return image
      //catch error if image doesn't exist
      try {
        return require(`../../../../src/Python/venv/Scripts/${this.informations.concours[this.$route.params.id].username}_profile_pic.jpg`);
      } catch (e) {
        console.log(e);
        return require(`../../../../src/Python/venv/Scripts/not_found.png`);
      }
    }
  }
}
</script>

<style scoped lang="scss">


.containerDetail {
  position: absolute;
  bottom: -50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: black;
  box-shadow: -1rem 0 3rem #000;
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  overflow: hidden;

}

.infos {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;

}

h1 {
  color: white;
  font-weight: 600;
  text-transform: uppercase;
  position: relative;
  animation: appear 1s ease-in-out, moveUp .5s ease-in-out 1s;
  animation-fill-mode: forwards;

}

.twelve {
  font-size: 26px;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
  width: 160px;
  text-align: center;
  margin: auto;
  white-space: nowrap;
  padding-bottom: 13px;
}

.twelve:before {
  background-color: darkorange;
  content: '';
  display: block;
  height: 3px;
  width: 75px;
  margin-bottom: 5px;
}

.twelve:after {
  background-color: darkorange;
  content: '';
  display: block;
  position: absolute;
  right: 0;
  bottom: 0;
  height: 3px;
  width: 75px;
  margin-bottom: 0.25em;
}

.sub {
  margin-top: 60px;
  display: flex;
  align-items: center;
  justify-content: space-around;
  width: 600px;
}

.line {
  height: 1px;
  width: 0px;
  background-color: white;
  justify-content: flex-end;
  animation: line .8s ease-in-out 1.2s forwards;
}

.image {
  opacity: 0;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  animation: fade .8s ease-in-out 1.2s forwards;
}

.description {
  opacity: 0;
  animation: fade .8s ease-in-out 1.2s forwards;
  margin-bottom: 20px;
}

.detail:first-child {
  animation: appearLeft 1s ease-in-out .8s forwards;
  opacity: 0;
}

.detail:nth-child(2) {
  animation: appearLeft 1s ease-in-out .7s forwards;
  opacity: 0;
}

.detail:nth-child(3) {
  animation: appearLeft 1s ease-in-out .6s forwards;
  opacity: 0;
}


@keyframes appear {
  0% {
    transform: translate(-230px, 300px);
    color: transparent;
    scale: 5;
  }
  100% {
    transform: translate(-230px, 300px);
    color: white;
    scale: 1;

  }
}

.circle {
  position: relative;
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background-color: transparent;
  overflow: hidden;
  color: white;
  font-size: 4rem;
  margin: 50px;
  opacity: 0;
  animation: appearRight .8s ease-in-out 1s forwards;
}

.circle a {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 100;
}

#circleLevel {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: greenyellow;
  transition: height 0.5s;

}

#circle_wave {
  position: absolute;
  bottom: -20px;
  animation: slide 5s linear infinite;
}

@keyframes slide {
  0% {
    transform: translateX(-100px);
  }
  100% {
    transform: translateX(-340px);
  }
}

@keyframes moveUp {
  0% {
    transform: translate(-230px,300px);
  }
  100% {
    transform: translate(-230px, 20px);
  }
}

@keyframes appearLeft {
  0% {
    opacity: 0;
    transform: translateX(-100%);
  }
  100% {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes appearRight {
  0% {
    opacity: 0;
    transform: translateX(100%);
  }
  100% {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes fade {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }

}

@keyframes line {
  0% {
    width: 0;
  }
  100% {
    width: 300px;
  }
}

@media screen and (max-width: 860px) {
  .twelve {
    left: 15%;
  }
}

@media screen and (max-width: 730px) {
  .containerDetail {
    flex-direction: column;
    overflow-y: visible;
    height: 100%;

  }
  .description {
    width: 80%;
    margin: auto;
  }
  .sub {
    flex-direction: column;
    width: 100%;
    :nth-child(2) {
      margin: 20px 0;
    }
  }
  .detail {
    align-items: center;
    display: flex;
    flex-flow: column;
  }
}

@media screen and (max-width: 650px){
  .twelve {
    top: 5%;
    text-wrap: normal;
  }
}

@media screen and (max-width: 470px) {
  .twelve {
    font-size: 20px;
    left: 40%;

  }
}

@media screen and (max-width: 400px) {
  .twelve {
    left: 45%;

  }
}

@media screen and (max-width: 375px) {
  .twelve {
    left: 50%;
  }
}
</style>