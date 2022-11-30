<template>
  <router-link class="why-us" to="course">
    <h2>Why Us?</h2>
    <CoreButton variant="secondary">
      Let's Get Personal
    </CoreButton>
  </router-link>
</template>

<style lang="scss" scoped>
.why-us {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  border-radius: 3rem;
  background-image: url('@/assets/img/panel_why-us.png');
  background-size: cover;
  grid-column: span 12;
  gap: 4rem;
  grid-row: span 6;

  button {
    transform: rotate(-2.6deg);
  }

  h2 {
    font-family: "Passion One", sans-serif;
    font-size: 8.4rem;
    line-height: 72.19%;
    transition: all 0.25s ease;
    transform: rotate(-2.6deg);
    text-align: center;
    color: var(--white);
    text-shadow: 8px 8px 0 var(--black);
    -webkit-text-stroke: 3px var(--black);
  }

  &:hover {
    h2, button {
      transform: scale(1.2, 1.2);
    }
  }
}
</style>