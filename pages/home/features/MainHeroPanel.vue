<template>
  <router-link class="main-hero" to="course">
    <Duotone color="Pink">
      <img alt="Students learning to code." src="@/assets/img/upleveled_4_2bit.avif"/>
    </Duotone>

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
  position: relative;
  display: flex;
  flex-direction: column;
  border: 0.3rem solid var(--Color-Black);
  border-radius: var(--BorderRadius-L);
  grid-column: span 12;
  grid-row: span 10;

  img {
    transition: all 0.25s ease;
  }

  .main-hero__top {
    display: flex;
    align-items: center;
    gap: 2rem;
    z-index: 10;
    padding: 4rem;
  }

  .main-hero__middle {
    display: flex;
    align-items: center;
    flex: 1;
    flex-direction: column;
    justify-content: center;
    transition: all 0.25s ease;
    gap: 3rem;
    z-index: 10;

    h1 {
      font-size: var(--FontSize-Chonky-Chonk);
      line-height: 72.19%;
      transition: all 0.25s ease;
      transform: rotate(-2.6deg);
      text-align: center;
      color: var(--Color-White);
    }

    h2 {
      font-size: var(--FontSize-Chonky-S);
      font-weight: var(--FontWeight-Black);
      line-height: 72.19%;
      transition: all 0.25s ease;
      transform: rotate(-2.6deg);
      text-align: center;
      color: var(--Color-White);
      text-shadow: var(--Shadow-Border), var(--Shadow-L);
    }
  }

  .main-hero__bottom {
    display: flex;
    justify-content: flex-end;
    z-index: 10;
    padding: 4rem;
  }

  &:hover {
    img {
      transform: scale(1.05, 1.05);
    }

    .main-hero__middle {
      gap: 6rem;

      h1, h2 {
        transform: scale(1.2, 1.2);
      }
    }
  }
}
</style>