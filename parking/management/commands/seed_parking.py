from django.core.management.base import BaseCommand
from parking.models import Floor, Sector, ParkingSpot

class Command(BaseCommand):
    help = "Cria andares, setores e vagas automaticamente"

    def handle(self, *args, **kwargs):
        self.stdout.write("Criando andares, setores e vagas...")

        floors = ["Térreo", "1º Andar", "2º Andar"]
        sectors = ["A", "B", "C"]

        for floor_name in floors:
            floor, _ = Floor.objects.get_or_create(name=floor_name)

            for sector_name in sectors:
                sector, _ = Sector.objects.get_or_create(
                    floor=floor,
                    name=sector_name
                )

                # Criar 10 vagas por setor
                for i in range(1, 11):
                    code = f"{sector_name}{i}"
                    ParkingSpot.objects.get_or_create(
                        sector=sector,
                        code=code
                    )

        self.stdout.write(self.style.SUCCESS("✔ Dados criados com sucesso!"))
