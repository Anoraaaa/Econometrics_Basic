from beta_1_and_0 import Beta

if __name__ == "__main__":
    weight = [51, 62, 69, 65, 65, 56, 66]
    height = [167, 182, 176, 173, 172, 175, 180]
    Feb_19 = Beta(weight,height)
    print(Feb_19.beta_1())
    print(Feb_19.beta_0())