<template>
  <section id="cta">
    <div class="cta__inner-wrapper">
      <h2>Ready... Steady... <span>Code!</span></h2>

      <div class="cta__options">
        <div class="cta__option">
          <h3>Ready to sign up?</h3>

          <p>
            We are excited to get to know you! Click apply and start your coding journey today.
          </p>

          <NuxtLink to="apply">
            <CoreButton backgroundColor="White" size="L" variant="secondary">
              Apply
            </CoreButton>
          </NuxtLink>
        </div>

        <div class="cta__option">
          <h3>Still unsure?</h3>

          <p>
            Looking for something else? Send us your questions or let us know what's holding you back.
          </p>

          <CoreButton backgroundColor="White" size="L" variant="secondary">
            Contact Us
          </CoreButton>
        </div>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
#cta {
  padding: 10rem 0 20rem 0;
  color: var(--Color-White);

  .cta__inner-wrapper {
    display: flex;
    align-items: center;
    flex-direction: column;
    max-width: var(--View-MaxWidth);
    margin: 0 auto;
    gap: 10rem;

    h2 {
      text-shadow: none;
      font-size: var(--FontSize-Chonky-M);
      font-weight: var(--FontWeight-Black);

      span {
        font-weight: var(--FontWeight-Black);
        background: var(--Gradient-PinkPurple);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
      }
    }

    .cta__options {
      display: grid;
      align-items: center;
      grid-auto-columns: 1fr;
      grid-auto-flow: column;
      grid-gap: 20rem;

      .cta__option {
        display: flex;
        align-items: center;
        flex: 1;
        flex-direction: column;
        gap: 3rem;

        h3 {
          font-size: var(--FontSize-XXL);
          font-weight: var(--FontWeight-Black);
        }

        p {
          font-size: var(--FontSize-M);
          font-weight: var(--FontWeight-Bold);
          max-width: 30rem;
          text-align: center;
        }
      }
    }
  }
}
</style>