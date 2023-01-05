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
          Lorem ipsum dolor sit amet. Eos pariatur amet aut iusto voluptatem eos consequatur molestiae et enim amet aut
          molestiae provident aut asperiores illum. In temporibus vitae sit facere veniam ut incidunt quod eum
          necessitatibus magnam eos rerum voluptatem!
          <br /><br />
          Qui tenetur quibusdam est unde quia quo velit corporis et minima sapiente et dicta aliquam eum labore
          consequatur. Ut sint explicabo hic rerum quibusdam At adipisci natus vel praesentium temporibus aut quia
          explicabo est veniam repellat eos dicta debitis.
          <br /><br />
          Est maxime nobis eum nihil consequatur aut eaque velit ab aspernatur dicta. Est aspernatur corrupti eum
          voluptatem placeat non reprehenderit molestias.
          Non harum voluptatem id galisum fugit 33 veniam quae sed nulla reprehenderit est dolor recusandae.
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
          background-image: url("assets/img/revolver-lane_2.avif");
          width: 34rem;
          height: 34rem;
          margin-top: -10rem;
        }

        &.--2 {
          background-image: url("assets/img/revolver-lane_1.avif");
          width: 28rem;
          height: 28rem;
          margin-top: -5rem;
          margin-left: 20rem;
        }

        &.--3 {
          background-image: url("assets/img/revolver-lane_3.avif");
          width: 34rem;
          height: 34rem;
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