<template>
  <div class="home">
    <section class="main container">
      <div class="main__blurb">
        <h1 class="main-blurb__header">
          a creative web agency<br>
          that makes the<br>
          <span>internet interesting</span>
        </h1>
        <p class="main-blurb__secondary">
          a <span>BOLD</span> & <span>MODERN</span> online presence has the power to <span>ENGAGE</span> users and
          brands through <span>UNIQUE</span> personality and a passion for the user experience. we <span>SOLVE</span>
          your online problems, and we have <span>FUN</span> doing it.
        </p>
        <router-link :to="{ name: 'Contact' }">
          <CTAButton text="let's create something" :rotation="-10"/>
        </router-link>
      </div>
      <div class="main__shapes">
        <img alt="Shapes" src="../assets/svg/shapes.svg"/>
      </div>
    </section>
    <section class="team container">
      <div class="team__avatar">
        <div class="team-avatar__wrapper">
          <div class="team-avatar__image">
            <img alt="Mitchell Romney" src="../assets/images/mitchell.jpg"/>
          </div>
          <div class="team-avatar__back"/>
        </div>
      </div>
      <div class="team__description">
        <div class="team__header">
          <span>The Team (Spoiler: It's Just Me)</span>
        </div>
        <div class="team__member">
          <div class="team-member__name">
            Mitchell Romney
          </div>
          <div class="team-member__position">
            Founder & Director
          </div>
          <div class="team-member__blurb">
            Mitchell Romney is a person. Mitchell Romney is a person. Mitchell Romney is a person. Mitchell Romney is a person.
            Mitchell Romney is a person. Mitchell Romney is a person. Mitchell Romney is a person. Mitchell Romney is a person.
            Mitchell Romney is a person. Mitchell Romney is a person. Mitchell Romney is a person. Mitchell Romney is a person.
          </div>
        </div>
      </div>
    </section>
    <section class="testimonials">
      <div class="testimonials__back-arrow" @click="cycleTestimonials('left')">
        <div class="icon-wrapper">
          <img alt="arrow-left" src="../assets/svg/arrow-left-solid.svg"/>
        </div>
      </div>
      <transition name="fade-left">
        <div class="testimonials__entry" v-if="!switchTestimonial">
          <div class="testimonial__avatar">
            <img alt="avatar" :src="getTestimonialAvatar(selectedTestimonial.image)"/>
          </div>
          <div class="testimonial__content">
            "{{ selectedTestimonial.testimonial }}"
          </div>
          <div class="testimonial__giver">
            <b>{{ selectedTestimonial.name }}</b>, {{ selectedTestimonial.position }}
            <span v-if="selectedTestimonial.company">@ {{ selectedTestimonial.company }}</span>
          </div>
        </div>
      </transition>
      <div class="testimonials__forward-arrow" @click="cycleTestimonials('right')">
        <div class="icon-wrapper">
          <img alt="arrow-right" src="../assets/svg/arrow-right-solid.svg"/>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { testimonials } from "@/assets/testimonials";
import CTAButton from "@/components/CTAButton"

export default {
  name: 'Home',
  components: {
    CTAButton
  },
  data() {
    return {
      testimonials: testimonials,
      switchTestimonial: false,
      selectedTestimonialIndex: Math.round(Math.random() * (testimonials.length - 1))
    }
  },
  computed: {
    selectedTestimonial() {
      return this.testimonials[this.selectedTestimonialIndex]
    }
  },
  methods: {
    cycleTestimonials(direction) {
      this.switchTestimonial = true
      const current = this.selectedTestimonialIndex

      this.selectedTestimonialIndex = direction === 'right'
          ? current + 1 === testimonials.length
              ? 0
              : current + 1
          : current === 0
              ? testimonials.length - 1
              : current - 1

      this.switchTestimonial = false
    },
    getTestimonialAvatar(path){
      return require(`../assets/images/${path}`)
    }
  }
}
</script>

<style scoped lang="scss">
@import '../styles/variables';

.home {
  section.main {
    display: flex;
    position: relative;
    height: calc(100vh - 200px);
    padding-top: 50px;
    padding-bottom: 50px;

    .main__blurb {
      width: 50%;

      .main-blurb__header {
        font-size: 52px;
        font-weight: bold;

        span {
          background-color: $rose;
        }
      }

      .main-blurb__secondary {
        font-size: 18px;

        span {
          font-weight: bold;
          color: $rose;
        }
      }
    }

    .main__shapes {
      margin-left: auto;
    }
  }

  section.team {
    background-color: $rose;
    padding-top: 50px;
    padding-bottom: 50px;
    display: grid;
    grid-template: auto / 1fr 1.5fr;
    grid-gap: 50px;

    .team__avatar {
      margin-left: auto;

      .team-avatar__wrapper {
        position: relative;

        .team-avatar__image {
          position: relative;
          height: 250px;
          width: 250px;
          border-radius: 50%;
          overflow: hidden;
          z-index: 100;

          img {
            height: 100%;
            width: auto;
          }
        }

        .team-avatar__back {
          position: absolute;
          top: 20px;
          left: 10px;
          height: 250px;
          width: 250px;
          background-color: $martinique;
          border-radius: 50%;
          z-index: 1;
        }
      }
    }

    .team__description {
      .team__header {
        font-weight: bold;
        text-transform: uppercase;

        span {
          background-color: $martinique;
        }
      }

      .team__member {
        .team-member__name {
          font-size: 34px;
          font-weight: bold;
        }

        .team-member__position {
          opacity: 0.9;
          font-size: 24px;
          font-weight: 500;
        }

        .team-member__blurb {
          font-size: 16px;
          opacity: 0.9;
          margin-top: 20px;
        }
      }
    }
  }

  section.testimonials {
    background-color: white;
    color: black;
    padding-top: 50px;
    padding-bottom: 50px;
    text-align: center;
    display: grid;
    grid-template: auto / 10% auto 10%;
    grid-template-areas: 'left entry right';
    height: 300px;
    align-items: center;

    .testimonials__back-arrow, .testimonials__forward-arrow {
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;

      .icon-wrapper {
        height: 20px;
        width: 20px;
      }
    }

    .testimonials__back-arrow {
      grid-area: left;
    }

    .testimonials__forward-arrow {
      grid-area: right;
    }

    .testimonials__entry {
      grid-area: entry;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-items: center;

      .testimonial__avatar {
        justify-self: center;
        height: 60px;
        width: 60px;
        border-radius: 50%;
        overflow: hidden;

        img {
          height: 100%;
          width: auto;
        }
      }

      .testimonial__content {
        font-size: 20px;
        padding: 0 10%;
        margin: 20px 0;
      }

      .testimonial__giver {
        font-size: 16px;
      }
    }
  }
}
</style>
