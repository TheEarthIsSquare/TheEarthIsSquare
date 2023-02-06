<template>
  <section id="quote-break">
    <div class="quote-break__content">
      <div class="quote">
        <strong>“You miss 100% of the shots<br/> you don’t take. - Wayne Gretzky”</strong>
        <strong>- Michael Scott</strong>
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
@import 'assets/style/variables.scss';

#quote-break {
  height: 15vh;
  border-radius: var(--BorderRadius-L);
  background: var(--Gradient-PinkPurple);

  @media screen and (max-width: $BreakPoint-Tablet) {
    height: auto;
  }

  .quote-break__content {
    display: grid;
    align-items: center;
    justify-content: center;
    max-width: var(--View-MaxWidth);
    height: 100%;
    margin: auto;
    padding-right: 10rem;
    color: var(--Color-White);
    grid-template-columns: auto 1fr;
    grid-gap: 5rem;

    @media screen and (max-width: $BreakPoint-Tablet) {
      text-align: center;
      grid-template-columns: 1fr;
      padding: 2rem;
      grid-gap: 1rem;
    }

    .quote {
      display: flex;
      align-items: flex-end;
      flex-direction: column;
      font-size: var(--FontSize-L);

      @media screen and (max-width: $BreakPoint-Tablet) {
        font-size: var(--FontSize-M);
        align-items: center;
      }

      strong {
        &:first-child {
          padding-right: 4rem;

          @media screen and (max-width: $BreakPoint-Tablet) {
            padding-right: 0;
          }
        }
      }
    }

    p {
      font-size: var(--FontSize-M);

      @media screen and (max-width: $BreakPoint-Tablet) {
        font-size: var(--FontSize-S);
      }
    }
  }
}
</style>