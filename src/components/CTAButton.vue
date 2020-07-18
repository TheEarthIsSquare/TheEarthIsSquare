<template>
  <button class="main-blurb__cta" :style="{ transform : `rotate(${rotation}deg)`}">
    <span class="main-blurb-cta__text">{{ text }}</span>
  </button>
</template>

<script>
export default {
  name: "CTAButton",
  props: {
    text: {
      type: String,
      required: true
    },
    rotation: {
      type: Number,
      default: 0
    }
  }
}
</script>

<style lang="scss" scoped>
.main-blurb__cta {
  margin: 50px;
  position: relative;
  background-color: transparent;
  color: white;
  font-weight: bold;
  font-size: 24px;
  border: 2px solid $rose;
  border-radius: 20px 20px 5px 20px;
  width: 180px;
  height: 60px;
  cursor: pointer;
  transition: background-color .25s ease;

  .main-blurb-cta__text {
    top: 10px;
    left: -60px;
    position: absolute;
    width: 300px;
    background-color: rgba($martinique, 1);
    transition: background-color .15s ease;
  }

  &:hover {
    background-color: $rose;
    transform: rotate(-10deg) scale(1.1, 1.1);

    .main-blurb-cta__text {
      background-color: rgba($martinique, 0);
    }
  }
}
</style>