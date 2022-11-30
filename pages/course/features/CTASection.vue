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

          <router-link to="apply">
            <CoreButton backgroundColor="white" size="L" variant="secondary">
              Apply
            </CoreButton>
          </router-link>
        </div>

        <div class="cta__option">
          <h3>Still unsure?</h3>

          <p>
            Looking for something else? Send us your questions or let us know what's holding you back.
          </p>

          <CoreButton backgroundColor="white" size="L" variant="secondary">
            Contact Us
          </CoreButton>
        </div>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
#cta {
  padding: 10rem 0;
  color: var(--white);

  .cta__inner-wrapper {
    display: flex;
    align-items: center;
    flex-direction: column;
    max-width: 144rem;
    margin: 0 auto;
    gap: 10rem;

    h2 {
      font-size: 6.484rem;
      font-weight: 900;

      span {
        font-weight: 900;
        background: linear-gradient(247.29deg, #EB2188 7.21%, #D909DD 91.17%);
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
          font-size: 3.583rem;
          font-weight: 900;
        }

        p {
          font-size: 1.728rem;
          font-weight: bold;
          max-width: 30rem;
          text-align: center;
        }
      }
    }
  }
}
</style>