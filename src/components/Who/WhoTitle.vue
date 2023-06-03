<template>
  <div class="containerInfos">
    <div class="content">
      <a>{{infos}} </a>
    </div>
  </div>
</template>

<script>
export default {
  name: "WhoTitle",
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

}
</script>

<style scoped>

.containerInfos {
  min-width: 400px;
  background-color: #000;
  background-image: none;
  border: 1px solid rgb(37,37,37);
  border-radius: 4px;
  box-shadow: #fff 4px 4px 0 0,#000 4px 4px 0 1px;
  box-sizing: border-box;
  color: #fff;
  display: inline-block;
  font-family: ITCAvantGardeStd-Bk,Arial,sans-serif;
  font-size: 30px;
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

@media (min-width: 768px) {
  .containerInfos {
    padding: 12px 50px;
  }
}

@media screen and (max-width: 500px) {
  .containerInfos {
    padding: 12px 50px;
    min-width: 200px;
    max-width: 300px;
    font-size: 20px;
  }
}

@media screen and (max-width: 410px) {
  .containerInfos {
    padding: 12px 30px;
    min-width: 180px;
    max-width: 200px;
    font-size: 15px;

  }


}
</style>
