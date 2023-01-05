<template>
  <section id="location">
    <div class="location__inner-wrapper">
      <div class="location__images">
        <div class="location__image --1" />
        <div class="location__image --2" />
        <div class="location__image --3" />
      </div>

      <div class="location__blurb">
        <h2>Welcome to our <span>home</span></h2>

        <img alt="Revolver Lane Logo" src="@/assets/img/revolver-lane_logo.png" />

        <p>
          When deciding where we were going to host our bootcamp to maximize creativity, motivation, and networking
          opportunities, it was a no-brainer to partner up with our friends at Revolver Lane for the space!
          <br /><br />
          Revolver Lane is a stunning co-working space located on Chapel St in Prahran, Melbourne. Their motto is
          "Work Weird", which is a fantastically creative energy to be learning modern web development in. The Earth Is Square
          marks creativity & "Thinking Outside The Square" as one of the most important skills to develop while
          learning to code.
          <br /><br />
          The location is also a perfect mix of the best of Melbourne, with amazing coffee hosted inside the co-working space,
          or dozens of cafes a couple minutes away for you to choose from before and during classes! Keen on a relaxing drink after
          working your ass off all day? Chapel St definitely has you covered with all the bars you'll need.
        </p>

        <h3>Want to attend remotely?</h3>
        <p>
          Can’t make it to class? Or maybe you’re outside of Melbourne? No problem! We have options for you. You can
          choose to be remote, come to the class, or even both! Our hybrid set up allows you to participate regardless
          of where you are.
        </p>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
#location {
  display: flex;
  justify-content: center;
  padding: 5rem 0;
  border-radius: var(--BorderRadius-L);
  background-color: var(--Color-White);

  .location__inner-wrapper {
    position: relative;
    max-width: var(--View-MaxWidth);

    .location__images {
      position: absolute;
      left: 0;

      .location__image {
        background-size: cover;
        border-radius: var(--BorderRadius-L);
        box-shadow: var(--Shadow-L);

        &.--1 {
          background-image: url("assets/img/revolver-lane_1.avif");
          width: 34rem;
          height: 34rem;
          margin-top: -10rem;
        }

        &.--2 {
          background-image: url("assets/img/revolver-lane_3.avif");
          width: 30rem;
          height: 30rem;
          margin-top: -5rem;
          margin-left: 20rem;
        }

        &.--3 {
          background-image: url("assets/img/revolver-lane_2.avif");
          width: 38rem;
          height: 38rem;
          margin-top: -5rem;
        }
      }
    }

    .location__blurb {
      display: flex;
      flex-direction: column;
      text-align: right;
      margin-left: 50%;

      h2 {
        color: var(--Color-Black);
        font-size: var(--FontSize-Chonky-S);
        text-shadow: none;

        span {
          color: var(--Color-Pink);
        }
      }

      img {
        height: 10rem;
        margin-bottom: 1rem;
        margin-left: auto;
      }

      p {
        font-size: var(--FontSize-M);
      }

      h3 {
        font-size: var(--FontSize-XXL);
        margin-top: 1rem;
      }
    }
  }
}
</style>