<template>
  <router-link class="become-a-developer__wrapper" to="course">
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
      <div class="become-a-developer__background" />
      <div class="become-a-developer__backdrop" />
    </div>
  </router-link>
</template>

<style lang="scss" scoped>
.become-a-developer__wrapper {
  overflow: hidden;
  color: var(--white);
  border: 0.3rem solid var(--white);
  border-radius: 3rem;
  grid-column: span 7;
  grid-row: span 5;

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
    border-radius: 3rem;
    gap: 3rem;

    &:hover {
      .become-a-developer__background {
        transform: scale(1.1, 1.1);
      }
    }

    .become-a-developer__backdrop {
      position: absolute;
      top: -100%;
      right: 60%;
      bottom: -100%;
      left: -50%;
      transform: rotate(-30deg);
      background-color: var(--black);
    }

    h2 {
      font-size: 3.2rem;
    }

    h3 {
      font-size: 1.8rem;
      opacity: 0.7;
    }

    button, h2, h3 {
      position: relative;
      z-index: 10;
      margin-right: auto;
    }

    .become-a-developer__background {
      position: absolute;
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
      transition: all 0.25s ease;
      background-image: url('@/assets/img/panel_become-a-developer.png');
      background-size: cover;
    }
  }
}
</style>