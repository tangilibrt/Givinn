<template>
  <div class="containerInfos">
    <div class="content">
      <a class="text">{{ infos }}</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "SoloConcoursInfoBlocBlanc",
  props: {
    infos: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
.containerInfos {
  min-width: 400px;
  max-width: 650px;
  max-height: 100px;
  background-color: white;
  background-image: none;
  border: 1px solid rgb(37, 37, 37);
  border-radius: 4px;
  box-shadow: #000 4px 4px 0 0, #fff 4px 4px 0 1px;
  box-sizing: border-box;
  color: #000;
  cursor: pointer;
  display: inline-block;
  font-family: ITCAvantGardeStd-Bk, Arial, sans-serif;
  font-size: 14px;
  font-weight: 400;
  line-height: 20px;
  overflow: hidden;
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

.content {
  position: relative;
  max-height: 80px;
  overflow: hidden;
  text-overflow: ellipsis;
}

.text {
  overflow: hidden;
  text-overflow: ellipsis;
  max-height: 100em;
  white-space: pre;
}

.containerInfos:focus {
  text-decoration: none;
}

.containerInfos:hover {
  text-decoration: none;
}

.containerInfos:active {
  box-shadow: rgba(0, 0, 0, 0.125) 0 3px 5px inset;
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
