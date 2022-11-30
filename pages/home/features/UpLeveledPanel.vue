<template>
  <a class="upleveled" href="https://upleveled.io" target="_blank">
    <h3>Powered By</h3>
    <img alt="UpLeveled Logo" src="@/assets/img/upleveled.png" />
    <CoreButton variant="secondary">
      Stalk Them
    </CoreButton>
  </a>
</template>

<style lang="scss" scoped>
.upleveled {
  font-size: 2.488rem;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  transition: all 0.25s ease;
  border-radius: 3rem;
  background-color: white;
  background-image: url('@/assets/img/panel_upleveled.png');
  background-size: cover;
  grid-column: span 12;
  grid-row: span 5;
  gap: 3rem;

  h3, img, button {
    transition: all 0.25s ease;
  }

  h3 {
    transform: rotate(-2.6deg);
    color: var(--white);
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