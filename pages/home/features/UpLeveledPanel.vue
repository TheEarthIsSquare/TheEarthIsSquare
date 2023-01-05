<template>
  <a class="upleveled" href="https://upleveled.io" target="_blank">
    <Duotone color="Green">
      <img alt="Students learning to code." src="@/assets/img/upleveled_8_2bit.avif"/>
    </Duotone>

    <h3>Powered By</h3>
    <img alt="UpLeveled Logo" src="@/assets/img/upleveled_logo.png" />
    <CoreButton variant="secondary">
      Stalk Them
    </CoreButton>
  </a>
</template>

<style lang="scss" scoped>
.upleveled {
  position: relative;
  font-size: var(--FontSize-L);
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  transition: all 0.25s ease;
  border-radius: var(--BorderRadius-L);
  grid-column: span 12;
  grid-row: span 5;
  gap: 3rem;

  h3, img, button {
    z-index: 10;
    transition: all 0.25s ease;
  }

  h3 {
    transform: rotate(-2.6deg);
    color: var(--Color-White);
  }

  button {
    transform: rotate(-2.6deg);
  }


  &:hover {
    h3, img, button {
      transform: scale(1.2, 1.2);
    }
  }
}
</style>