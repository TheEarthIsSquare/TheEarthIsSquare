<template>
  <a class="location" href="https://revolverlane.com" target="_blank">
    <h2>Welcome To Our Home</h2>
    <div class="location__logo">
      <img alt="Revolver Lane Logo" src="@/assets/img/revolver-lane.png" />
    </div>
  </a>
</template>

<style lang="scss" scoped>
.location {
  display: flex;
  overflow: hidden;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  transition: all 0.25s ease;
  border-radius: 3rem;
  background-image: url('@/assets/img/panel_location.png');
  background-size: cover;
  grid-column: span 8;
  grid-row: span 5;
  gap: 2rem;

  h2 {
    font-size: 4.2rem;
    font-weight: 900;
    line-height: 72.19%;
    transition: all 0.25s ease;
    transform: rotate(-2.6deg);
    text-align: center;
    color: var(--white);
    text-shadow: 5px 5px 0 var(--black);
    -webkit-text-stroke: 3px var(--black);
  }

  .location__logo {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 120%;
    margin-right: -10%;
    margin-left: -10%;
    padding: 1rem 0;
    transition: all 0.25s ease;
    transform: rotate(-2.6deg);
    border: 0.3rem solid var(--black);
    background-color: var(--white);
    box-shadow: 8px 8px 0 var(--black);

    img {
      width: 30%;
      height: auto;
      margin-top: -0.5rem;
    }
  }

  &:hover {
    gap: 4rem;

    h2, .location__logo {
      transform: scale(1.2, 1.2);
    }
  }
}
</style>