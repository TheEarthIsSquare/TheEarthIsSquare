<template>
  <NuxtLink class="why-us" to="course">
    <Duotone color="Purple">
      <img alt="Students learning to code." src="~/assets/img/upleveled_12_2bit.avif"/>
    </Duotone>

    <h2>Why Us?</h2>
    <CoreButton variant="secondary">
      Let's Get Personal
    </CoreButton>
  </NuxtLink>
</template>

<style lang="scss" scoped>
.why-us {
  position: relative;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: center;
  border-radius: var(--BorderRadius-L);
  grid-column: span 12;
  gap: 4rem;
  grid-row: span 6;

  img {
    transition: all 0.25s ease;
  }

  button {
    transform: rotate(-2.6deg);
  }

  h2 {
    font-family: "Passion One", sans-serif;
    font-size: var(--FontSize-Chonky-XL);
    line-height: 72.19%;
    transition: all 0.25s ease;
    transform: rotate(-2.6deg);
    text-align: center;
    color: var(--Color-White);
    text-shadow: var(--Shadow-Border), var(--Shadow-L);
  }

  &:hover {
    img {
      transform: scale(1.05, 1.05);
    }

    h2, button {
      transform: scale(1.2, 1.2);
    }
  }
}
</style>