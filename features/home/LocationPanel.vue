<template>
  <a class="location" href="https://revolverlane.com" target="_blank">
    <Duotone color="Pink">
      <img alt="Revolver Lane" src="~/assets/img/revolver-lane_2_2bit.avif"/>
    </Duotone>

    <h2>Welcome To Our Home</h2>
    <div class="location__logo">
      <img alt="Revolver Lane Logo" src="~/assets/img/revolver-lane_logo.png"/>
    </div>
  </a>
</template>

<style lang="scss" scoped>
.location {
  position: relative;
  display: flex;
  overflow: hidden;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  transition: all 0.25s ease;
  border-radius: var(--BorderRadius-L);
  grid-column: span 8;
  grid-row: span 5;
  gap: 2rem;

  img {
    transition: all 0.25s ease;
  }

  h2 {
    font-size: var(--FontSize-Chonky-S);
    line-height: 72.19%;
    transition: all 0.25s ease;
    transform: rotate(-2.6deg);
    text-align: center;
    color: var(--Color-White);
  }

  .location__logo {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 120%;
    margin-right: -10%;
    margin-left: -10%;
    padding: 2rem 0;
    transition: all 0.25s ease;
    transform: rotate(-2.6deg);
    border: 0.3rem solid var(--Color-Black);
    background-color: var(--Color-White);
    box-shadow: var(--Shadow-L);
    z-index: 10;

    img {
      width: 20%;
      height: auto;
      margin-top: -0.5rem;
    }
  }

  &:hover {
    img {
      transform: scale(1.05, 1.05);
    }

    gap: 4rem;

    h2, .location__logo {
      transform: scale(1.2, 1.2);
    }
  }
}
</style>