<template>
  <NuxtLink class="become-a-developer__wrapper" to="course">
    <Duotone color="Blue">
      <img alt="Students learning to code." src="~/assets/img/upleveled_5_2bit.avif"/>
    </Duotone>

    <div class="become-a-developer">
      <CoreButton variant="secondary">
        Learn More
      </CoreButton>

      <Heading :customStyle="{ opacity: 0.7 }" type="h5">
        Our hands-on Web Development Bootcamp will not only teach you cutting-edge technologies.
      </Heading>

      <Heading type="h4">
        Become A Developer<br/>
        In 3 Months
      </Heading>

      <div class="become-a-developer__backdrop"/>
    </div>
  </NuxtLink>
</template>

<style lang="scss" scoped>
@import 'assets/style/variables.scss';

.become-a-developer__wrapper {
  position: relative;
  overflow: hidden;
  color: var(--Color-White);
  border: 0.3rem solid var(--Color-White);
  border-radius: var(--BorderRadius-L);
  grid-column: span 7;
  grid-row: span 5;

  @media screen and (max-width: $BreakPoint-Tablet) {
    grid-column: span 12;
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

    button {
      margin-right: auto;
    }

    .become-a-developer__backdrop {
      position: absolute;
      top: -100%;
      right: 60%;
      bottom: -100%;
      left: -50%;
      transform: rotate(-30deg);
      background-color: var(--Color-Black);
    }
  }
}
</style>