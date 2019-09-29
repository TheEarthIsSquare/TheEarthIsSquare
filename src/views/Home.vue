<template>
    <div id="home">
        <div class="main">
            <img alt="The Earth is Square Logo" src="../assets/Logo.png">
            <span class="blurb">
        We're getting a makeover.
      </span>
        </div>
        <div class="contact">
            <div class="emoji">
                ✉️
            </div>
            <span
                    @click="doCopy"
                    content="Copied!"
                    v-tippy="{trigger : 'click'}">hello@theearthissquare.com</span>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'home',
        data: function () {
            return {
                message: 'hello@theearthissquare.com'
            }
        },
        methods: {
            doCopy: function () {
                this.$copyText(this.message);
            }
        }
    }
</script>

<style scoped lang="scss">
    #home {
        height: 100vh;
        width: 100vw;
        display: flex;
        align-items: center;
        justify-content: center;

        .main {
            width: 90%;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;

            @media #{$bp-md}{
                width: 35%;
            }

            img {
                width: 100%;
                height: auto;
                margin-bottom: 20px;
            }

            .blurb {
                color: white;
                background-color: #FE5186;
                font-size: 1.5rem;
                font-weight: bold;
            }
        }

        .contact {
            position: absolute;
            bottom: 50px;
            text-align: center;

            @media #{$bp-md}{
                text-align: right;
                right: 50px;
            }


            .emoji {
                font-size: 5rem;
            }

            span {
                background-color: #D90ADD;
                color: white;
                font-size: 2rem;
                cursor: pointer;
            }
        }
    }
</style>