<template>
   <div class="containerInfos" @click="redirect">
     <div class="content">
       <a>{{infos}} </a>
     </div>
   </div>
</template>

<script>
export default {
  name: "SoloConcoursInfoBloc",
  props: {
    infos: {
      type: String,
      required: true
      },
    link: {
      type: String,
      required: false
      },
    },
  methods: {
    redirect() {
      // redirect to the internet page on instagram in link if link is not null
      if (this.link != null) {
        window.open(this.link, '_blank');
      }
    }
  }
}
</script>

<style scoped>

.containerInfos {
  width: 400px;
  background-color: #000;
  background-image: none;
  border: 1px solid rgb(37,37,37);
  border-radius: 4px;
  box-shadow: #fff 4px 4px 0 0,#000 4px 4px 0 1px;
  box-sizing: border-box;
  color: #fff;
  cursor: pointer;
  display: inline-block;
  font-family: ITCAvantGardeStd-Bk,Arial,sans-serif;
  font-size: 14px;
  font-weight: 400;
  line-height: 20px;
  overflow: visible;
  padding: 12px 40px;
  text-align: center;
  text-transform: none;
  touch-action: manipulation;
  user-select: none;
  -webkit-user-select: none;
  vertical-align: middle;
  white-space: nowrap;
  margin: 10px 5px 10px 0;
}

.containerInfos:focus {
  text-decoration: none;
}

.containerInfos:hover {
  text-decoration: none;
}

.containerInfos:active {
  box-shadow: rgba(0, 0, 0, .125) 0 3px 5px inset;
  outline: 0;
}

.containerInfos:not([disabled]):active {
  box-shadow: #fff 2px 2px 0 0, #000 2px 2px 0 1px;
  transform: translate(2px, 2px);
}


@media (min-width: 768px) {
  .containerInfos {
    padding: 12px 50px;
  }
}
</style>
