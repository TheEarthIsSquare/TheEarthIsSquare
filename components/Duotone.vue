<template>
  <div class="duotone-wrapper">
    <slot/>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
  color: {
    type: String,
    required: true
  },
  backgroundColor: {
    type: String,
    default: "Black"
  }
})

const mainColor = computed(() => `var(--Color-Duotone${props.color})`);
const bgColor = computed(() => `var(--Color-${props.backgroundColor})`);
</script>

<style lang="scss">
.duotone-wrapper {
  background-color: v-bind(mainColor);
  display: flex;
  flex: 1 1 100%;
  height: 100%;
  overflow: hidden;
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  border-radius: var(--BorderRadius-L);

  img {
    filter: grayscale(100%) contrast(1) blur(var(--blur));
    flex: 1 0 100%;
    height: 100%;
    max-width: 100%;
    mix-blend-mode: multiply;
    object-fit: cover;
    position: relative;
    width: 100%;
    transition: all 0.25s ease;

    &:hover {
      transform: scale(1.05, 1.05);
    }
  }

  &::before {
    background-color: v-bind(bgColor);
    bottom: 0;
    content: '';
    height: 100%;
    left: 0;
    mix-blend-mode: lighten;
    position: absolute;
    right: 0;
    top: 0;
    width: 100%;
    z-index: 1;
  }
}
</style>