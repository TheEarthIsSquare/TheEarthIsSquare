<template>
  <router-link class="become-a-developer__wrapper" to="course">
    <Duotone color="Blue">
      <img alt="Students learning to code." src="@/assets/img/upleveled_5_2bit.avif"/>
    </Duotone>

    <div class="become-a-developer">
      <CoreButton variant="secondary">
        Learn More
      </CoreButton>

      <h3>
        Our hands-on Web Development Bootcamp will not only teach you cutting-edge technologies.
      </h3>

      <h2>
        Become A Developer<br />
        In 3 Months
      </h2>
      <div class="become-a-developer__backdrop" />
    </div>
  </router-link>
</template>

<style lang="scss" scoped>
.become-a-developer__wrapper {
  position: relative;
  overflow: hidden;
  color: var(--Color-White);
  border: 0.3rem solid var(--Color-White);
  border-radius: var(--BorderRadius-L);
  grid-column: span 7;
  grid-row: span 5;

  img {
    transition: all 0.25s ease;
  }

  &:hover {
    img {
      transform: scale(1.05, 1.05);
    }
  }

  .become-a-developer {
    position: relative;
    display: flex;
    overflow: hidden;
    flex-direction: column;
    justify-content: center;
    height: 100%;
    padding-right: 60%;
    padding-left: 2rem;
    transition: all 0.25s ease;
    border-radius: var(--BorderRadius-L);
    gap: 3rem;

    .become-a-developer__backdrop {
      position: absolute;
      top: -100%;
      right: 60%;
      bottom: -100%;
      left: -50%;
      transform: rotate(-30deg);
      background-color: var(--Color-Black);
    }

    h2 {
      font-size: var(--FontSize-XXL);
    }

    h3 {
      font-size: var(--FontSize-M);
      opacity: 0.7;
    }

    button, h2, h3 {
      position: relative;
      z-index: 10;
      margin-right: auto;
    }
  }
}
</style>