<template>
  <NuxtLink :style="style" :target="isExternalLink ? '_blank' : ''" :to="to" class="panel">
    <slot name="bg"/>

    <div class="panel__top">
      <slot name="top"/>
    </div>

    <div :style="{ gap: midGap }" class="panel__mid">
      <slot/>
    </div>

    <div class="panel__bot">
      <slot name="bot"/>
    </div>
  </NuxtLink>
</template>

<script lang="ts" setup>
const props = defineProps({
  to: {
    type: String,
    required: true
  },
  colSpan: {
    type: String,
    required: true,
  },
  rowSpan: {
    type: String,
    required: true,
  },
  isExternalLink: {
    type: Boolean,
    default: false
  },
  midGap: {
    type: String,
    default: "4rem"
  }
})

const style = computed(() => ({
  gridColumn: `span ${props.colSpan}`,
  gridRow: `span ${props.rowSpan}`
}))
</script>

<style lang="scss" scoped>
@import 'assets/style/variables.scss';

.panel {
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  flex-direction: column;
  position: relative;
  border-radius: var(--BorderRadius-L);
  padding: 4rem;
  overflow: hidden;

  &:hover {
    button {
      transform: scale(1.2, 1.2);
    }
  }

  @media screen and (max-width: $BreakPoint-Tablet) {
    padding: 2rem;
    border-radius: var(--BorderRadius-S);
  }

  .panel__top {
    display: flex;
    align-items: center;
    gap: 1rem;
    width: 100%;
  }

  .panel__mid {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    text-align: center;
    width: 100%;
    flex: 1;
    transform: rotate(-2.6deg);
  }

  .panel__bot {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 4rem;
    width: 100%;
  }
}
</style>