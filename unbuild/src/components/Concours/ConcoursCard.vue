<template>
  <div class="card" ref="card" @mouseover="detColor" @click="goToDetails">
    <h3 class="title" ref="title">{{ concours.username }}</h3>
    <div class="bar" ref="bar">
      <div class="emptybar" ref="emptybar"></div>
      <div id="filledbar" ref="filledbar" :style="{maxWidth : concours.confidence}"></div>
    </div>
    <div class="circle" ref="circle">
      <svg ref="svgc" version="1.1" xmlns="http://www.w3.org/2000/svg">
        <circle class="stroke" cx="60" cy="60" r="50" />
      </svg>
      <img class="image" ref="image" :src="getImageUrl" alt="image"/>
    </div>
    <div class="enSavoirPlus" ref="enSavoirPlus">
      <a>En savoir plus</a>
      <a>En savoir plus</a>
      <a>En savoir plus</a>
      <a>En savoir plus</a>
      <a>En savoir plus</a>
      <a>En savoir plus</a>
      <a>En savoir plus</a>

    </div>
  </div>

</template>

<script>
export default {
  name: "ConcoursCard",
  props: {
    concours: {
      type: Object,
      required: true
    },
  },
  computed: {
    getImageUrl() {
      // if image exist : return image
      //catch error if image doesn't exist
      try{
        return require(`../../../src/Python/venv/Scripts/${this.concours.username}_profile_pic.jpg`);
      }
      catch (e){
        console.log(e);
        return require(`../../../src/Python/venv/Scripts/not_found.png`);
      }
    }
  },
  methods: {
    detColor(){
      if (this.concours.intConfidence < 25){
        console.log("red");
        this.$refs.filledbar.style.background = "red";
      }
      else if (this.concours.intConfidence < 50){
        console.log("orange");
        this.$refs.filledbar.style.background = "linear-gradient(90deg, rgba(255,119,0,1) 0%, rgba(255,98,0,1) 46%, rgba(255,201,0,1) 100%)";
      }
      else if (this.concours.intConfidence < 75){
        console.log("yellow");
        this.$refs.filledbar.style.background = "linear-gradient(90deg, rgba(255,188,0,1) 0%, rgba(249,255,0,1) 48%, rgba(189,255,0,1) 100%)";
      }

      else if (this.concours.intConfidence < 100){
        console.log("green");
        this.$refs.filledbar.style.background = "linear-gradient(90deg, rgba(207,255,0,1) 0%, rgba(39,255,0,1) 21%, rgba(138,170,49,1) 100%)";
      }
      else{
        document.getElementById("filledbar").style.background = "linear-gradient(90deg, rgba(0,154,217,1) 0%, rgba(217,147,0,1) 65%, rgba(255,186,0,1) 100%)";
      }
    },
    goToDetails(){
      this.$refs.card.style.transform = "scale(15)";
      this.$refs.card.style.borderRadius = "1000px";
      this.$refs.card.style.zIndex = "1000";
      this.$refs.svgc.style.transform = "scale(0)";
      this.$refs.title.style.transform = "scale(0)";
      this.$refs.bar.style.transform = "scale(0)";
      this.$refs.enSavoirPlus.style.transform = "scale(0)";
      setTimeout(() => {

        this.$router.push({name: "concours detail", params: {id: this.concours.username}});
      }, 500);

    }
  },

}
</script>

<style scoped lang="scss">

.card {
  display: flex;
  height: 280px;
  width: 300px;
  background-color: black;
  border-radius: 10px;
  box-shadow: -1rem 0 3rem #000;
  /*   margin-left: -50px; */
  transition: 0.5s ease-out;
  position: relative;
  margin: 20px;
  overflow: hidden;
  cursor: pointer;
}

.card:not(:first-child) {
  margin-left: -50px;
}

.card:hover {
  transform: translateY(-20px);
  transition: 0.4s ease-out;

  #filledbar {
    width:100%;
    transition: 0.4s ease-in-out;
  }

  .stroke {
    stroke-dashoffset: 100;
    transition: 0.6s ease-out;
  }
  .enSavoirPlus {
    animation: esp 10s linear infinite;

  }
}

.card:hover ~ .card {
  position: relative;
  left: 50px;
  transition: 0.4s ease-out;
}

.title {
  color: white;
  font-weight: 300;
  position: absolute;
  left: 20px;
  top: 15px;
}

.bar {
  position: absolute;
  top: 100px;
  left: 20px;
  height: 5px;
  width: 150px;
}

.emptybar {
  background-color: #2e3033;
  width: 100%;
  height: 100%;
}

#filledbar {
  position: absolute;
  top: 0px;
  z-index: 3;
  width: 0;
  height: 100%;
  background: rgb(255,0,0);
  background: linear-gradient(90deg, rgba(0,154,217,1) 0%, rgba(217,147,0,1) 65%, rgba(255,186,0,1) 100%);
  transition: 0.6s ease-out;
}


.circle {
  position: absolute;
  top: 150px;
  left: calc(50% - 60px);
}

.circle img {
  position: absolute;
  top: 23px;
  left: 23px;
  width: 75px;
  height: 75px;
  border-radius: 50%;
  border: 5px solid white;
  box-shadow: 0 0 0 5px #2e3033;
}

.stroke {
  stroke: white;
  stroke-dasharray: 360;
  stroke-dashoffset: 360;
  transition: 0.6s ease-out;
}

svg {
  fill: #17141d;
  stroke-width: 2px;
};

.enSavoirPlus {
  position: absolute;
  top: -140px;
  right: -130px;
  width: 100%;
  color: white;
  font-weight: 300;
  font-size: 12px;
  white-space: nowrap;
  overflow: visible;
  transform: translateY(166.16px) rotate(90deg);



  :not(:last-child) {
    margin-right: 5px;

  }

  :nth-child(2n) {
    -webkit-text-stroke: 0.01em #fff;
    color: transparent;
  }
}

@keyframes esp {
  0% {
    transform: translateY(0px) rotate(90deg);
  }
  100% {

    transform: translateY(166.16px) rotate(90deg);
  }
}

@keyframes goToDetails {
  0% {
    transform: translateY(0px);
  }
  100% {
    transform: translateY(-1000px);
  }
}

</style>