<template>
  <router-link class="why-code" to="course">
    <h2>Why Learn<br /> To Code?</h2>
    <CoreButton variant="secondary">
      Discover The Secrets
    </CoreButton>
  </router-link>
</template>

<style lang="scss" scoped>
.why-code {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  border-radius: 3rem;
  background-image: url('@/assets/img/panel_why-code.png');
  background-size: cover;
  grid-row: span 8;
  gap: 4rem;
  grid-column: span 12;

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