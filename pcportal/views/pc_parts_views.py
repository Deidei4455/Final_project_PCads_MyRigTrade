from django.shortcuts import render
from django.core.paginator import Paginator

from ..models.part_models import Cpu, Gpu, Psu, Ram, Storage, CasePC, Motherboard, CpuCooler


def get_all_parts(request):
    """
    This function retrieves all parts
    and renders them in all parts page.
    """
    cpu_list = Cpu.objects.all()
    gpu_list = Gpu.objects.all()
    psu_list = Psu.objects.all()
    ram_list = Ram.objects.all()
    storage_list = Storage.objects.all()
    casepc_list = CasePC.objects.all()
    motherboard_list = Motherboard.objects.all()
    cpucooler_list = CpuCooler.objects.all()

    tab = request.GET.get('tab', 'cpu')
    page_number = request.GET.get('page')

    paged_cpu_list = (Paginator(cpu_list, 6)).get_page(page_number)
    paged_gpu_list = (Paginator(gpu_list, 6)).get_page(page_number)
    paged_psu_list = (Paginator(psu_list, 6)).get_page(page_number)
    paged_ram_list = (Paginator(ram_list, 6)).get_page(page_number)
    paged_storage_list = (Paginator(storage_list, 6)).get_page(page_number)
    paged_casepc_list = (Paginator(casepc_list, 6)).get_page(page_number)
    paged_motherboard_list = (Paginator(motherboard_list, 6)).get_page(page_number)
    paged_cpucooler_list = (Paginator(cpucooler_list, 6)).get_page(page_number)

    context_my = {
        'cpu_list': paged_cpu_list,
        'gpu_list': paged_gpu_list,
        'psu_list': paged_psu_list,
        'ram_list': paged_ram_list,
        'storage_list': paged_storage_list,
        'casepc_list': paged_casepc_list,
        'motherboard_list': paged_motherboard_list,
        'cpucooler_list': paged_cpucooler_list,
        'active_tab': tab
    }
    return render(request, 'parts.html', context=context_my)
