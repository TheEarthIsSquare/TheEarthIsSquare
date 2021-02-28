<template>
  <div id="home">
    <BackgroundTextWrapper id="test">
      <div class="text">
        {{ backgroundText }} <span>{{ backgroundText }}</span>
      </div>
    </BackgroundTextWrapper>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { BackgroundTextWrapper } from "@/views/Home/style/BackgroundTextWrapper";

export default defineComponent({
  name: 'Home',
  components: {
    BackgroundTextWrapper,
  },
  setup() {
    return {
      backgroundText: 'THINK OUTSIDE THE SQUARE'
    }
  }
})
</script>

<style lang="scss" scoped>
#home {
  min-height: 100vh;
  background-image: -moz-element(#test);
  background-repeat: repeat-y;
  background-position: center;
}
</style>
