<template>
  <router-link class="main-hero" to="course">
    <div class="main-hero__top">
      <CoreButton variant="secondary">
        231 Chapel Street, Prahran
      </CoreButton>
      <CoreButton variant="secondary">
        April 17 - July 7
      </CoreButton>
    </div>

    <div class="main-hero__middle">
      <h1>THE EARTH<br />IS SQUARE</h1>
      <h2>WEB DEVELOPMENT BOOTCAMP</h2>
    </div>

    <div class="main-hero__bottom">
      <CoreButton size="L" variant="secondary">
        Enrolments Open
      </CoreButton>
    </div>
  </router-link>
</template>

<style lang="scss" scoped>
.main-hero {
  display: flex;
  flex-direction: column;
  padding: 5rem;
  border-radius: 3rem;
  background-image: url('@/assets/img/main_hero.png');
  background-size: cover;
  grid-column: span 12;
  grid-row: span 10;

  .main-hero__top {
    display: flex;
    align-items: center;
    gap: 2rem;
  }

  .main-hero__middle {
    display: flex;
    align-items: center;
    flex: 1;
    flex-direction: column;
    justify-content: center;
    transition: all 0.25s ease;
    gap: 3rem;

    h1 {
      font-size: 110px;
      line-height: 72.19%;
      transition: all 0.25s ease;
      transform: rotate(-2.6deg);
      text-align: center;
      color: var(--white);
      text-shadow: 8px 8px 0 var(--black);
      -webkit-text-stroke: 3px var(--black);
    }

    h2 {
      font-size: 43.53px;
      font-weight: 900;
      line-height: 72.19%;
      transition: all 0.25s ease;
      transform: rotate(-2.6deg);
      text-align: center;
      color: var(--white);
      text-shadow: 5px 5px 0 var(--black);
      -webkit-text-stroke: 3px var(--black);
    }
  }

  .main-hero__bottom {
    display: flex;
    justify-content: flex-end;
  }

  &:hover {
    .main-hero__middle {
      gap: 6rem;

      h1, h2 {
        transform: scale(1.2, 1.2);
      }
    }
  }
}
</style>