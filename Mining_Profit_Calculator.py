def calculate_mining_profit(hashrate, power_consumption, electricity_cost, crypto_price, block_reward, pool_fee):
    """
    Вычисляет прибыль от майнинга.
    
    Параметры:
        hashrate: Скорость майнинга в MH/s.
        power_consumption: Потребление электроэнергии в ваттах.
        electricity_cost: Стоимость электроэнергии за кВт⋅ч.
        crypto_price: Текущая цена криптовалюты в USD.
        block_reward: Награда за блок (в монетах).
        pool_fee: Комиссия пула в %.
    
    Возвращает:
        Чистую прибыль в USD.
    """
    # Перевод хешрейта в GH/s для расчёта
    hashrate_gs = hashrate / 1000  # Примерная формула для сети
    daily_income = hashrate_gs * block_reward * crypto_price
    
    # Учитываем комиссию пула
    daily_income_after_fee = daily_income * (1 - pool_fee / 100)
    
    # Вычисление расходов на электроэнергию
    daily_power_cost = (power_consumption / 1000) * 24 * electricity_cost
    
    # Чистая прибыль
    daily_profit = daily_income_after_fee - daily_power_cost
    return daily_profit

def main():
    print("=== Калькулятор прибыли от майнинга ===")
    hashrate = float(input("Введите скорость майнинга (MH/s): "))
    power_consumption = float(input("Введите потребление энергии (Вт): "))
    electricity_cost = float(input("Введите стоимость электроэнергии ($/кВт⋅ч): "))
    crypto_price = float(input("Введите текущую цену криптовалюты ($): "))
    block_reward = float(input("Введите награду за блок (в монетах): "))
    pool_fee = float(input("Введите комиссию пула (%): "))
    
    daily_profit = calculate_mining_profit(
        hashrate, power_consumption, electricity_cost, crypto_price, block_reward, pool_fee
    )
    print(f"\nЧистая прибыль в день: ${daily_profit:.2f}")

if __name__ == "__main__":
    main()

