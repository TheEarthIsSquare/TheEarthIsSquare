<template>
  <section id="location">
    <div class="location__inner-wrapper">
      <div class="location__images">

      </div>

      <div class="location__blurb">
        <h2>Welcome to our <span>home</span></h2>

        <img alt="Revolver Lane Logo" src="@/assets/img/revolver-lane.png" />

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
  border-radius: 3rem;
  background-color: var(--white);

  .location__inner-wrapper {
    display: grid;
    max-width: 144rem;
    grid-template-columns: 1fr 1fr;

    .location__images {

    }

    .location__blurb {
      display: flex;
      flex-direction: column;
      text-align: right;

      h2 {
        font-size: 6.484rem;

        span {
          color: var(--pink);
        }
      }

      img {
        height: 10rem;
        margin-bottom: 1rem;
        margin-left: auto;
      }

      p {
        font-size: 1.728rem;
      }

      h3 {
        font-size: 3.583rem;
        margin-top: 1rem;
      }
    }
  }
}
</style>