<template>
  <component :is="type" :style="style">
    <slot/>
  </component>
</template>

<script lang="ts" setup>
import { PropType } from "@vue/runtime-core";

const props = defineProps({
  type: {
    type: String as PropType<"h1" | "h2" | "h3" | "h4" | "h5" | "h6">,
    required: true
  },
  font: {
    type: String as PropType<"PassionOne" | "Raleway">,
    default: "Raleway"
  },
  customStyle: {
    type: Object,
    default: {}
  }
})

const style = computed(() => ({
  fontFamily: `${props.font === "PassionOne" ? 'Passion One, ' : ''}'Raleway', sans-serif`,
  ...props.customStyle
}))
</script>

<style lang="scss" scoped>
@import 'assets/style/variables.scss';

h1, h2, h3, h4, h5, h6 {
  z-index: 10;
  transition: all 0.25s ease;

  &:hover {
    transform: scale(1.2, 1.2);
  }
}

h1 {
  color: var(--Color-White);
  text-shadow: var(--Shadow-Border), var(--Shadow-L);
  font-weight: var(--FontWeight-Black);
  font-size: var(--FontSize-Chonky-Chonk);
  line-height: 72%;

  @media screen and (max-width: $BreakPoint-Tablet) {
    font-size: var(--FontSize-Chonky-M);
  }
}

h2 {
  font-size: var(--FontSize-Chonky-Chonk);
  font-weight: var(--FontWeight-Black);
  line-height: 72%;
  color: var(--Color-White);
  text-shadow: var(--Shadow-Border), var(--Shadow-L);

  @media screen and (max-width: $BreakPoint-Desktop) {
    font-size: var(--FontSize-Chonky-L);
  }

  @media screen and (max-width: $BreakPoint-Tablet) {
    font-size: var(--FontSize-Chonky-M);
    text-shadow: var(--Shadow-Border), var(--Shadow-M);
  }
}

h3 {
  font-size: var(--FontSize-Chonky-S);
  font-weight: var(--FontWeight-Black);
  color: var(--Color-White);
  text-shadow: var(--Shadow-Border), var(--Shadow-L);

  @media screen and (max-width: $BreakPoint-Tablet) {
    font-size: var(--FontSize-XL);
    text-shadow: var(--Shadow-Border), var(--Shadow-M);
  }
}

h4 {
  font-size: var(--FontSize-XXL);
  font-weight: var(--FontWeight-Bold);
  color: var(--Color-White);
  text-shadow: var(--Shadow-Border), var(--Shadow-L);


  @media screen and (max-width: $BreakPoint-Desktop) {
    font-size: var(--FontSize-L);
    text-shadow: var(--Shadow-Border), var(--Shadow-M);
  }
}

h5 {
  font-size: var(--FontSize-M);
  font-weight: var(--FontWeight-Bold);
  color: var(--Color-White);

  @media screen and (max-width: $BreakPoint-Desktop) {
    font-size: var(--FontSize-S);
  }
}

h6 {

}
</style>