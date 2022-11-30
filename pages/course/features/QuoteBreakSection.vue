<template>
  <section id="quote-break">
    <div class="quote-break__content">
      <div class="quote">
        <h3>“You miss 100% of the shots<br /> you don’t take. - Wayne Gretzky”</h3>
        <h3>- Michael Scott</h3>
      </div>
      <p>
        We know that a career transition is a tough step to take. But we believe this journey is worth it. Our dynamic
        curriculum and hands-on structure will not only teach you cutting edge technologies – our immersive bootcamp
        prepares you for a multitude of roles in tech companies and gives you the skills to build products for your
        own business.
      </p>
    </div>
  </section>
</template>

<style lang="scss" scoped>
#quote-break {
  height: 15vh;
  border-radius: 3rem;
  background: linear-gradient(247.29deg, #EB2188 7.21%, #D909DD 91.17%);

  .quote-break__content {
    display: grid;
    align-items: center;
    justify-content: center;
    max-width: 144rem;
    height: 100%;
    margin: auto;
    padding-right: 10rem;
    color: var(--white);
    grid-template-columns: auto 1fr;
    grid-gap: 5rem;

    .quote {
      display: flex;
      align-items: flex-end;
      flex-direction: column;

      h3 {
        font-size: 2.488rem;

        &:first-child {
          padding-right: 4rem;
        }
      }
    }

    p {
      font-size: 1.728rem;
      padding-right: 10rem;
    }
  }
}
</style>